# Provide the data or objects needed for the test

import pytest
import requests
import json

@pytest.fixture
def registered_candidate():
    """Registers a test candidate and returns the candidate ID."""
    BASE_URL = "http://127.0.0.1:5000"
    data = {"candidate_id": "test_cand_1", "name": "Test Candidate 1"}
    headers = {"Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/register_candidate", headers=headers, data=json.dumps(data))
    assert response.status_code == 200
    return "test_cand_1"

@pytest.fixture
def registered_voter():
    """Registers a test voter and returns the voter ID."""
    BASE_URL = "http://127.0.0.1:5000"
    data = {"voter_id": "test_voter_1"} # Data voter can be adjust if there are another field
    headers = {"Content-Type": "application/json"}
    #Endpoint for registration voter need to be implement with the server
    #the endpoint assumption is /register_voter
    response = requests.post(f"{BASE_URL}/register_voter", headers=headers, data=json.dumps(data))
    assert response.status_code == 200
    return "test_voter_1"