from flask import Flask, request, jsonify
from blockchain import BitcoinTestnet
from ipfs_utils import IPFSClient
import hashlib
import os
from config import settings

app = Flask(__name__)

# Setup Blockchain Testnet and IPFS Client
BITCOIN_CLIENT = BitcoinTestnet(settings.RPC_USER, settings.RPC_PASSWORD)
IPFS_CLIENT = IPFSClient()

# In-memory storage for candidates and votes (for prototyping)
candidates = {}
votes = {}

@app.route("/register_candidate", methods=["POST"])
def register_candidate():
    data = request.json
    candidate_id = data.get("candidate_id")
    name = data.get("name")

    if not candidate_id or not name:
        return jsonify({"error": "Missing candidate_id or name"}), 400

    if candidate_id in candidates:
        return jsonify({"error": "Candidate already exists"}), 400

    candidates[candidate_id] = name
    return jsonify({"message": "Candidate registered successfully", "candidate_id": candidate_id, "name": name})

@app.route("/vote", methods=["POST"])
def vote():
    data = request.json
    voter_id = data.get("voter_id")
    candidate_id = data.get("candidate_id")

    if not voter_id or not candidate_id:
        return jsonify({"error": "Missing voter_id or candidate_id"}), 400

    if candidate_id not in candidates:
        return jsonify({"error": "Candidate does not exist"}), 404

    if voter_id in votes:
        return jsonify({"error": "Voter has already voted"}), 400

    # Record vote
    votes[voter_id] = candidate_id

    # Store vote metadata on IPFS and Blockchain
    metadata = f"Voter: {voter_id}, Candidate: {candidate_id}"
    try:
        # Save metadata to IPFS
        ipfs_hash = IPFS_CLIENT.add_data(metadata)

        # Store IPFS hash on Bitcoin Testnet
        result = BITCOIN_CLIENT.store_metadata(ipfs_hash)
        return jsonify({
            "message": "Vote successfully recorded",
            "txid": result["txid"],
            "ipfs_hash": ipfs_hash
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/results", methods=["GET"])
def results():
    tally = {}
    for candidate_id in votes.values():
        if candidate_id not in tally:
            tally[candidate_id] = 0
        tally[candidate_id] += 1

    results = {candidates[cid]: count for cid, count in tally.items()}
    return jsonify({"results": results})

@app.route("/get_vote_metadata", methods=["GET"])
def get_vote_metadata():
    ipfs_hash = request.args.get("ipfs_hash")

    if not ipfs_hash:
        return jsonify({"error": "Missing IPFS hash"}), 400

    try:
        output_path = IPFS_CLIENT.get_file(ipfs_hash, "metadata_output.txt")
        with open(output_path, "r") as f:
            metadata_content = f.read()
        return jsonify({"metadata": metadata_content})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
