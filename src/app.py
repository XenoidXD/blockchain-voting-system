from flask import Flask, request, jsonify
from blockchain import BitcoinTestnet
from ipfs_utils import IPFSClient
from config import settings
import hashlib
import os
import json
from datetime import datetime

app = Flask(__name__)

# Setup Blockchain Testnet and IPFS Client
BITCOIN_CLIENT = BitcoinTestnet(settings.RPC_USER, settings.RPC_PASSWORD)
IPFS_CLIENT = IPFSClient(settings.IPFS_HTTP_API)

# In-memory storage for candidates and votes (for prototyping)
candidates = {}
votes = {}

@app.route("/register_candidate", methods=["POST"])
def register_candidate():
    data = request.json
    candidate_id = data.get("candidate_id")
    name = data.get("name")

    if not candidate_id or not name:
        return jsonify({"status": "error", "error": "Missing candidate_id or name"}), 400

    if candidate_id in candidates:
        return jsonify({"status": "error", "error": "Candidate already exists"}), 400

    candidates[candidate_id] = name
    return jsonify({"status": "success", "data": {"candidate_id": candidate_id, "name": name}})

@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    voter_id = data.get("voter_id")
    candidate_id = data.get("candidate_id")

    if not voter_id or not candidate_id:
        return jsonify({"status": "error", "error": "Missing voter_id or candidate_id"}), 400

    if candidate_id not in candidates:
        return jsonify({"status": "error", "error": "Candidate does not exist"}), 404

    if voter_id in votes:
        return jsonify({"status": "error", "error": "Voter has already voted"}), 400

    # Record vote
    votes[voter_id] = candidate_id

    # Store vote metadata on IPFS and Blockchain
    metadata = {
        "voter_id": voter_id,
        "candidate_id": candidate_id,
        "timestamp": datetime.utcnow().isoformat()
    }
    try:
        # Save metadata to IPFS
        metadata_json = json.dumps(metadata)
        ipfs_hash = IPFS_CLIENT.add_data(metadata_json)

        # Store IPFS hash on Bitcoin Testnet
        result = BITCOIN_CLIENT.store_metadata(ipfs_hash)
        return jsonify({
            "status": "success",
            "data": {
                "txid": result["txid"],
                "ipfs_hash": ipfs_hash
            }
        })
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500

@app.route("/results", methods=["GET"])
def results():
    tally = {}
    for candidate_id in votes.values():
        if candidate_id not in tally:
            tally[candidate_id] = 0
        tally[candidate_id] += 1

    results = {candidates[cid]: count for cid, count in tally.items()}
    return jsonify({"status": "success", "data": {"results": results}})

@app.route("/get_vote_metadata", methods=["GET"])
def get_vote_metadata():
    ipfs_hash = request.args.get("ipfs_hash")

    if not ipfs_hash:
        return jsonify({"status": "error", "error": "Missing IPFS hash"}), 400

    try:
        output_path = IPFS_CLIENT.get_file(ipfs_hash, "metadata_output.txt")
        with open(output_path, "r") as f:
            metadata_content = f.read()
        return jsonify({"status": "success", "data": {"metadata": metadata_content}})
    except Exception as e:
        return jsonify({"status": "error", "error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=os.getenv("FLASK_DEBUG", "False") == "True")
