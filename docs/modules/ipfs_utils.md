# ipfs_utils Module Documentation

This module provides utilities for interacting with the IPFS network. It uses the `ipfshttpclient` library to communicate with a local or remote IPFS node.

## Classes

### `IPFSClient(ipfs_http_api)`

A class for interacting with the IPFS network.

*   **Parameters:**
    *   `ipfs_http_api` (str): The HTTP API address of the IPFS node (e.g., `/ip4/127.0.0.1/tcp/5001`).

## Methods

### `add_json(data)`

Adds JSON data to IPFS.

*   **Parameters:**
    *   `data` (dict or list): The JSON data to add.
*   **Returns:**
    *   `str` or `None`: The IPFS hash (CID) of the added data, or `None` if an error occurs.
*   **Raises:**
    *   `ipfshttpclient.exceptions.ErrorResponse`: If there's an issue with the IPFS API.
*   **Example Usage:**

    ```python
    from ipfs_utils import IPFSClient

    ipfs = IPFSClient("/ip4/127.0.0.1/tcp/5001")
    metadata = {"voter_id": "123", "candidate_id": "456"}
    cid = ipfs.add_json(metadata)
    if cid:
        print(f"Metadata added to IPFS with CID: {cid}")
    else:
        print("Failed to add metadata to IPFS")
    ```

### `get_json(cid)`

Retrieves JSON data from IPFS given its CID.

*   **Parameters:**
    *   `cid` (str): The IPFS Content Identifier (CID).
*   **Returns:**
    *   `dict` or `list` or `None`: The retrieved JSON data, or `None` if the CID is not found or an error occurs.
*   **Raises:**
    *   `ipfshttpclient.exceptions.ErrorResponse`: If there's an issue with the IPFS API.

*   **Example Usage:**

    ```python
    from ipfs_utils import IPFSClient

    ipfs = IPFSClient("/ip4/127.0.0.1/tcp/5001")
    metadata = ipfs.get_json("Qm...") # Replace with a valid CID
    if metadata:
        print(f"Retrieved metadata: {metadata}")
    else:
        print("Failed to retrieve metadata from IPFS")
    ```

[Documentasikan method-method lain yang ada di `ipfs_utils.py`, misalnya fungsi untuk verifikasi data dari IPFS, dll.]

## Error Handling

The module handles potential errors by catching `ipfshttpclient.exceptions.ErrorResponse` exceptions and returning `None` or raising them as appropriate. Ensure proper error handling in your application when using these functions.