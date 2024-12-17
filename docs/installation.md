# Installation Guide

This guide provides step-by-step instructions for setting up and running the Blockchain-Based Voting System.

## Prerequisites

*   Python 3.8+
*   Bitcoin Core with Testnet enabled (and RPC configured)
*   IPFS client (local or remote, e.g., Infura, Pinata)
*   `pip` (Python package installer)

## Steps

1.  Clone the repository:

    ```bash
    git clone <repository_url>
    cd blockchain-voting-system
    ```

2.  Create a virtual environment (recommended):

    ```bash
    python3 -m venv venv      # Linux/macOS
    venv\Scripts\activate     # Windows
    ```

3.  Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4.  Configuration:
    * Copy `config/credentials.template.json` to `config/credentials.json`.
    * Edit `config/credentials.json` to include your Bitcoin RPC credentials and IPFS HTTP API address. The format should be:

    ```json
    {
    "bitcoin_rpc_user": "your_rpc_user",
    "bitcoin_rpc_password": "your_rpc_password",
        "ipfs_http_api": "/ip4/127.0.0.1/tcp/5001" //Or a remote gateway IPFS endpoint if needed
    }
    ```
5. Create a `.env` file. Put the `FLASK_APP=app.py` in the file.

6.  Run the application:

    ```bash
    flask run
    ```

7. Access the application in your web browser at `http://127.0.0.1:5000`.