# config Module Documentation

This module handles application configuration, loading credentials, and setting constants in BVS (blockchain-voting-system)

## Modules/Files

### `settings.py`

This module reads configuration settings from environment variables and the `credentials.json` file.

## Variables

*   `RPC_USER` (str): The Bitcoin RPC username.
*   `RPC_PASSWORD` (str): The Bitcoin RPC password.
*   `FLASK_PORT` (int): The port on which the Flask application runs (default: 5000).
* `IPFS_HTTP_API` (str): The address of the IPFS API.
*   `DEBUG` (bool): Whether the application is running in debug mode.

## `credentials.json`

This file stores sensitive credentials (should not be committed to version control). It should have the following format:

```json
{
  "bitcoin_rpc_user": "your_rpc_user",
  "bitcoin_rpc_password": "your_rpc_password",
    "ipfs_http_api": "/ip4/127.0.0.1/tcp/5001"
}