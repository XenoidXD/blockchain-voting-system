# API Documentation

This document describes the API endpoints available in the Blockchain-Based Voting System.

## Endpoints

### 1. Register Candidate (`/register_candidate`)

Registers a new candidate.

*   **Method:** `POST`
*   **Request Body (JSON):**

    ```json
    {
      "candidate_id": "unique_candidate_id", // Required, unique identifier for the candidate
      "name": "Candidate Name"                // Required, the name of the candidate
    }
    ```

*   **Response (JSON):**
    *   **Success (200 OK):**

        ```json
        {
          "message": "Candidate registered successfully.",
          "candidate_id": "unique_candidate_id",
            "name": "Candidate Name"
        }
        ```

    *   **Error (400 Bad Request - Missing parameters):**

        ```json
        {
          "error": "Missing candidate_id or name."
        }
        ```
    *   **Error (409 Conflict - Candidate Already Exists):**

        ```json
        {
          "error": "Candidate with this ID already exists."
        }
        ```

### 2. Cast Vote (`/vote`)

Casts a vote for a candidate.

*   **Method:** `POST`
*   **Request Body (JSON):**

    ```json
    {
      "voter_id": "voter_unique_id",        // Required, unique identifier for the voter
      "candidate_id": "candidate_unique_id" // Required, ID of the candidate to vote for
    }
    ```

*   **Response (JSON):**
    *   **Success (200 OK):**

        ```json
        {
          "message": "Vote cast successfully.",
          "ipfs_hash": "Qm...",              // IPFS hash of the vote metadata
            "transaction_id" : "0x..."       // ID of the transaction in Bitcoin testnet
        }
        ```

    *   **Error (400 Bad Request - Missing parameters):**

        ```json
        {
          "error": "Missing voter_id or candidate_id."
        }
        ```
    *   **Error (404 Not Found - Invalid candidate ID):**

         ```json
        {
          "error": "Candidate with this ID Not Found."
        }
        ```

### 3. Get Results (`/results`)

Retrieves the current vote counts.

*   **Method:** `GET`
*   **Response (JSON):**

    ```json
    {
      "results": {
        "candidate_id_1": 10, // Number of votes for candidate 1
        "candidate_id_2": 15, // Number of votes for candidate 2
        // ...
      }
    }
    ```
    *   **Error (500 Internal Server Error - Error fetching results):**

        ```json
        {
          "error": "Error Fetching Results."
        }
        ```

### 4. Get Vote Metadata (`/get_vote_metadata`)

Retrieves vote metadata from IPFS given its CID.

*   **Method:** `GET`
*   **Query Parameters:**
    *   `ipfs_hash`: The IPFS hash (CID) of the metadata.
*   **Response (JSON):**
    *   **Success (200 OK):**

        ```json
        {
          "voter_id": "voter_unique_id",
          "candidate_id": "candidate_unique_id"
        }
        ```

    *   **Error (404 Not Found):**

        ```json
        {
          "error": "IPFS hash not found."
        }
        ```
    *   **Error (500 Internal Server Error - Error fetching metadata):**

        ```json
        {
          "error": "Error Fetching Metadata."
        }
        ```