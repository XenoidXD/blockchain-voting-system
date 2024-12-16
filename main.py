# Blockchain Voting System
# Description: A prototype voting system using blockchain to ensure transparency and security.

import hashlib
import json
import requests
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from flask import Flask, request, jsonify
from ipfshttpclient import connect

# Initialize Flask app
app = Flask(__name__)

# Bitcoin Testnet RPC Configuration
BITCOIN_RPC_USER = "your_rpc_user"
BITCOIN_RPC_PASSWORD = "your_rpc_password"
BITCOIN_RPC_HOST = "127.0.0.1"
BITCOIN_RPC_PORT = 18332
rpc_url = f"http://{BITCOIN_RPC_USER}:{BITCOIN_RPC_PASSWORD}@{BITCOIN_RPC_HOST}:{BITCOIN_RPC_PORT}"

# Initialize RPC connection
try:
    rpc_connection = AuthServiceProxy(rpc_url)
except Exception as e:
    print(f"Error connecting to Bitcoin RPC: {e}")

# Connect to IPFS
try:
    ipfs_client = connect()
except Exception as e:
    print(f"Error connecting to IPFS: {e}")

# Global variable to store voting data
election_data = {
    "candidates": {},
    "votes": {},
    "blockchain_records": []
}

# Helper function to hash data
def hash_data(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

# API Routes

@app.route("/register_candidate", methods=["POST"])
def register_candidate():
    data = request.json
    candidate_id = hash_data(data["name"])

    if candidate_id not in election_data["candidates"]:
        election_data["candidates"][candidate_id] = data["name"]
        return jsonify({"message": "Candidate registered successfully.", "id": candidate_id}), 200
    else:
        return jsonify({"message": "Candidate already registered."}), 400

@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    voter_id = hash_data(data["voter_id"])
    candidate_id = data["candidate_id"]

    if voter_id in election_data["votes"]:
        return jsonify({"message": "Voter has already voted."}), 400

    if candidate_id not in election_data["candidates"]:
        return jsonify({"message": "Invalid candidate."}), 400

    election_data["votes"][voter_id] = candidate_id

    # Record transaction in Bitcoin Testnet
    try:
        metadata = {
            "voter_id_hash": voter_id,
            "candidate_id": candidate_id,
            "candidate_name": election_data["candidates"][candidate_id]
        }
        metadata_json = json.dumps(metadata)
        ipfs_hash = ipfs_client.add_str(metadata_json)

        txid = rpc_connection.sendtoaddress("mipcBbFg9gMiCh81Kj8tqqdgoZub1ZJRfn", 0.0001, "Voting metadata", "", False, "", "UNSET", False, ipfs_hash)

        election_data["blockchain_records"].append({"ipfs_hash": ipfs_hash, "txid": txid})
    except JSONRPCException as rpc_error:
        return jsonify({"message": "Error recording vote in blockchain.", "error": str(rpc_error)}), 500
    except Exception as e:
        return jsonify({"message": "Unexpected error.", "error": str(e)}), 500

    return jsonify({"message": "Vote recorded successfully.", "txid": txid, "ipfs_hash": ipfs_hash}), 200

@app.route("/results", methods=["GET"])
def results():
    tally = {}

    for voter, candidate_id in election_data["votes"].items():
        if candidate_id not in tally:
            tally[candidate_id] = 0
        tally[candidate_id] += 1

    results = {
        "tally": {election_data["candidates"][k]: v for k, v in tally.items()},
        "total_votes": len(election_data["votes"]),
        "blockchain_records": election_data["blockchain_records"]
    }

    return jsonify(results), 200

# Main Entry
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
