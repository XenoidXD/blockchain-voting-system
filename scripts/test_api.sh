# Script to test the api 

#!/bin/bash

#Define Base URL
BASE_URL="http://127.0.0.1:5000"

# Register a test Candidate
curl -X POST -H "Content-Type: application/json" \
     -d '{"candidate_id": "testCand1", "name": "Test Candidate 1"}' \
     $BASE_URL/register_candidate

# Cast a Vote
curl -X POST -H "Content-Type: application/json" \
     -d '{"voter_id": "testVoter1", "candidate_id": "testCand1"}' \
     $BASE_URL/vote

# Get results
curl $BASE_URL/results

# Test endpoint to retrieve metadata of the vote
curl "$BASE_URL/get_vote_metadata?ipfs_hash=Qm..." # Replace with valid ipfs hash