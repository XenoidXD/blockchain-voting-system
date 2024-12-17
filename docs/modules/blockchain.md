# blockchain.py Module Documentation

This module defines the `BitcoinTestnet` class for interacting with the Bitcoin Testnet.

## Classes

### `BitcoinTestnet(rpc_user, rpc_password)`

A class for interacting with the Bitcoin Testnet via RPC.

*   **Parameters:**
    *   `rpc_user` (str): The Bitcoin RPC username.
    *   `rpc_password` (str): The Bitcoin RPC password.

## Methods

### `generate_address()`

Generates a new Bitcoin Testnet address.

*   **Returns:**
    *   `str`: The newly generated Bitcoin Testnet address.
*   **Raises:**
    *   `RuntimeError` if there's an issue with the RPC call.

### `get_balance(address)`

Retrieves the balance of a Bitcoin Testnet address.

*   **Parameters:**
    *   `address` (str): The Bitcoin Testnet address.
*   **Returns:**
    *   `float`: The balance of the address.
*   **Raises:**
    *   `RuntimeError` if there's an issue with the RPC call.

### `store_metadata(data)`

Stores metadata on the Bitcoin Testnet using OP_RETURN transactions.

*   **Parameters:**
    *   `data` (str): The metadata to store.
*   **Returns:**
    *   `dict`: A dictionary containing the transaction ID (`txid`) and the metadata hash (`metadata_hash`).
*   **Raises:**
    *   `RuntimeError` if there's an issue storing the metadata.

[Documentasikan method-method lainnya (jika ada) dengan format yang sama.]