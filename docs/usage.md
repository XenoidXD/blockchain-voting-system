# Usage Guide

This guide explains how to use the Blockchain-Based Voting System.

## Overview

The application provides a simple API for interacting with the voting system. The primary functions include registering candidates, casting votes, and viewing results. You can interact with this API programmatically or by building a front-end that consumes it.

## Core Functionality

### 1. Registering a Candidate

To register a candidate, send a `POST` request to the `/register_candidate` endpoint with the candidate's ID and name in JSON format (see [api.md](api.md) for detailed request and response formats).

**Example using `curl`:**

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"candidate_id": "cand001", "name": "John Doe"}' \
     http://127.0.0.1:5000/register_candidate
```

### 2. Casting a Vote
To cast a vote, send a `POST` request to the `/vote` endpoint with the voter's ID and the candidate's ID in JSON format (see [api.md](api.md) for details).

**Example using `curl`:**

```bash
curl -X POST -H "Content-Type: application/json" \
     -d '{"voter_id": "voter123", "candidate_id": "cand001"}' \
     http://127.0.0.1:5000/vote
```

### 3. Viewing Results
To get the current vote counts, send a `GET` request to the `/results` endpoint (see [api.md](api.md)).

**Example using `curl`:**

```bash
curl http://127.0.0.1:5000/results
```

### 4. Retrieving Vote Metadata
To retrieve metadata associated with a vote from IPFS (using its CID), send a `GET` request to the `/get_vote_metadata` endpoint and provide the `ipfs_hash` parameter (see [api.md](api.md)).

**Example using `curl`:**

```bash
curl "http://127.0.0.1:5000/get_vote_metadata?ipfs_hash=QmW..." # Replace with valid ipfs hash
```

## Developing a User Interface
This system relies on a simple backend API. You could create a user interface using any web framework or language which would then communicate with these endpoints. This allows the separation of concern and making the system very adaptable.

## Example Workflow
1. Create Candidates using `/register_candidate` endpoint.
2. Users/Voters use an interface (web page that make calls the api) to cast votes calling `/vote` endpoint.
3. Results are available through the `/results` endpoint at any time.
4. The provenance of each vote is available on the blockchain by retriving IPFS hash from the transaction and the vote information can then be checked from IPFS using `/get_vote_metadata`.