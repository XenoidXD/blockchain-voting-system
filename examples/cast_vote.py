import requests
import json

# Base URL of the API
BASE_URL = "http://127.0.0.1:5000"

def cast_vote(voter_id, candidate_id):
    """Casts a vote for a candidate using the API."""
    url = f"{BASE_URL}/vote"
    headers = {"Content-Type": "application/json"}
    data = {"voter_id": voter_id, "candidate_id": candidate_id}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error casting vote: {e}")
        if response is not None:
             print(f"Response content: {response.text}")
        return None

if __name__ == "__main__":
    voter_id = input("Enter voter ID: ")
    candidate_id = input("Enter candidate ID: ")

    result = cast_vote(voter_id, candidate_id)

    if result:
        print("Vote cast successfully:")
        print(json.dumps(result, indent=4))
    else:
        print("Vote casting failed.")