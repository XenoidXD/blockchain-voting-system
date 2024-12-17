import pytest
import requests
import json

BASE_URL = "http://127.0.0.1:5000"

def test_register_candidate():
    """Tests the /register_candidate endpoint."""
    data = {"candidate_id": "test_cand_2", "name": "Test Candidate 2"} #test dengan data berbeda
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/register_candidate", headers=headers, data=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["message"] == "Candidate registered successfully"

def test_cast_vote(registered_candidate,registered_voter): # menggunakan fixture registered_candidate
    """Tests the /vote endpoint."""
    candidate_id = registered_candidate
    voter_id = registered_voter
    data = {"voter_id": voter_id, "candidate_id": candidate_id}
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/vote", headers=headers, data=json.dumps(data))
    assert response.status_code == 200
    assert response.json()["message"] == "Vote cast successfully"

def test_get_results():
    """Tests the /results endpoint. Ensures response is a dictionary."""
    response = requests.get(f"{BASE_URL}/results")
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

def test_get_vote_metadata():
    """
    Tests the /get_vote_metadata endpoint.
    REPLACE "Qm..." with a valid IPFS hash for testing.
    Add more detailed assertions based on the expected metadata structure.
    """
    ipfs_hash = "Qm..." # Ganti dengan hash IPFS yang valid!
    response = requests.get(f"{BASE_URL}/get_vote_metadata", params={"ipfs_hash": ipfs_hash})
    assert response.status_code == 200
    #Contoh detail assertion
    #if response.status_code == 200:
    #    metadata = response.json()
    #    assert "voter_id" in metadata
    #    assert "candidate_id" in metadata