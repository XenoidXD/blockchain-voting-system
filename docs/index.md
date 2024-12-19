# Blockchain-Based Voting System

This project implements a secure and transparent voting system using blockchain technology. It provides API endpoints for managing candidates, casting votes, and retrieving results. The project also includes unit tests and a basic structure for incorporating blockchain logic.

## Project Structure
```bash
├── config/
│   ├── __init_.py                  # Marks that the config directory is a Python package
│   ├── credentials_template.json   # Store sensitive credential information
│   └── settings.py                 # Non-sensitive application settings, such as debug mode, API URLs, ports
├── docs/
│   ├── modules
│   |   ├── app.md                  # src/app.py documentation
│   |   ├── blockchain.md           # src/blockchain.py documentation
│   |   ├── config.md               # /config documentation
│   |   ├── ipfs_utils.md           # src/ipfs_utils.py documentation 
│   ├── api.md                      # API endpoint documentation
│   ├── architecture.md             # High-level system architecture
│   ├── index.md                    # Main project documentation
│   ├── installation.md             # Project installation instructions
│   └── usage.md                    # Usage examples and tutorials
├── examples
│   ├── cast_vote.py                # Example of casting a vote via API
│   ├── get_result.py               # Example of retrieving vote results via API
│   ├── get_vote_metadata.py        # Example of retrieving vote metadata via API
│   └── register_candidate.py       # Example of registering a candidate via API
├── scripts/
│   ├── deploy.sh                   # Script to deploy application
│   ├── run_dev_server.sh           # Script to run the development server
│   ├── setup_venv.sh               # Script to setup virtual environment
│   └── test_api.sh                 # Script to test API using curl
├── src/
|   ├── app.py                      # Main application file (Flask API)
|   ├── blockchain.py               # Blockchain logic implementation
|   └── ipfs_utils.py               # Utilities for interacting with IPFS
├── tests/                          
│   ├── conftest.py                 # Fixtures for tests
│   ├── test_api.py                 # Tests for API endpoints
│   └── test_blockchain.py          # Tests for blockchain logic
├── README.md                       # Project description and setup instructions
```

## Getting Started

### Prerequisites

*   Python 3.8+
*   pip (Python package installer)
*   Git (for version control)

### Installation

1.  Clone the repository:

    ```bash
    git clone [https://www.github.com/XenoidXD/blockchain-voting-system.git]
    ```

2.  Navigate to the project directory:

    ```bash
    cd blockchain-voting-system
    ```

3.  Create and activate a virtual environment:

    ```bash
    python3 -m venv venv          # Create a virtual environment
    source venv/bin/activate    # Activate (Linux/macOS)
    venv\Scripts\activate.bat   # Activate (Windows)
    ```
   You can also execute `scripts/setup_venv.sh` to automatically setup the virtual environment.

4.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Application

You can use `scripts/run_dev_server.sh` to run the application, or using this command

```bash
python app.py
```
The API will be accessible at `http://127.0.0.1:5000`.

## API Endpoints

### Register Candidate
**Endpoint**: /register_candidate
**Method**: POST
**Request Body (JSON)**:
```json
{
    "candidate_id": "candidate123",
    "name": "Candidate Name"
} 
```
**Response(JSON)**:
```json
{
    "message": "Candidate registered successfully"
}
```

### Cast Vote
**Endpoint**: /vote
**Method**: POST
**Request Body (JSON)**:
```json
{
    "voter_id": "voter456",
    "candidate_id": "candidate123"
}
```
**Response(JSON)**:
```json
{
    "message": "Vote cast successfully"
}
```

### Get Results
**Endpoint**: /results
**Method**: GET
**Response (JSON)**:
```json
{
    "candidate123": 10,
    "candidate456": 5
    // ... other candidates and their vote counts
}
```

### Get Vote Metadata
**Endpoint**: /get_vote_metadata
**Method**: GET
**Query Parameter**: ipfs_hash (The IPFS hash of the vote metadata)
**Response (JSON)**: Returns the vote metadata associated with the given IPFS hash. Example:
```json
{
   "voter_id": "voter456",
   "candidate_id": "candidate123",
   "timestamp": "2024-10-27 10:00:00",
   // other related information
}
```
## Testing
Run unit tests using `pytest`:
```bash
pytest
```
or you can use `scripts/test_api.sh` to test API endpoint
```bash
./scripts/test_api.sh
```

## Blockchain Integration (Optional)
The blockchain.py file provides a basic structure for incorporating blockchain logic. This can be extended to implement features such as:

- Storing votes on a blockchain.
- Verifying the integrity of the vote count.
- Decentralized vote management.

# License
[Detail check on the file License](../LICENSE)
