# Code example to get voting result

import requests
import json

# Base URL of the API
BASE_URL = "http://127.0.0.1:5000"

def get_results():
    """Retrieves election results using the API."""
    url = f"{BASE_URL}/results"
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error getting results: {e}")
        if response is not None:
             print(f"Response content: {response.text}")
        return None

if __name__ == "__main__":
    results = get_results()
    if results:
        print("Election Results:")
        print(json.dumps(results, indent=4))
    else:
        print("Failed to get results.")