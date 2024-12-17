import requests
import json

# Base URL of the API
BASE_URL = "http://127.0.0.1:5000"

def get_vote_metadata(ipfs_hash):
    """Retrieves metadata of a vote from IPFS using the API."""
    url = f"{BASE_URL}/get_vote_metadata"
    params = {"ipfs_hash": ipfs_hash}
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting vote metadata: {e}")
        if response is not None:
             print(f"Response content: {response.text}")
        return None

if __name__ == "__main__":
    ipfs_hash = input("Enter IPFS hash: ")

    metadata = get_vote_metadata(ipfs_hash)

    if metadata:
        print("Vote Metadata:")
        print(json.dumps(metadata, indent=4))
    else:
        print("Failed to get vote metadata.")