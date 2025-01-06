# Code example to register candidate

import requests
import json

# Base URL of the API
BASE_URL = "http://127.0.0.1:5000"

def register_candidate(candidate_id, name):
    """Registers a new candidate using the API."""
    url = f"{BASE_URL}/register_candidate"
    headers = {"Content-Type": "application/json"}
    data = {"candidate_id": candidate_id, "name": name}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()  # Raise an exception for bad status codes (4xx or 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error registering candidate: {e}")
        if response is not None:
             print(f"Response content: {response.text}")

        return None

if __name__ == "__main__":
    candidate_id = input("Enter candidate ID: ")
    candidate_name = input("Enter candidate name: ")

    result = register_candidate(candidate_id, candidate_name)

    if result:
        print("Candidate registered successfully:")
        print(json.dumps(result, indent=4))
    else:
        print("Candidate registration failed.")