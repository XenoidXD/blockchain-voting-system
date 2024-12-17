# System Architecture

This document describes the architecture of the Blockchain-Based Voting System.

## Overview

The system is designed using a modular architecture, integrating several key components:

1.  **Web Application (Flask):** Provides the user interface for interaction with the system (candidate registration, voting, result viewing).
2.  **Bitcoin Testnet:** Acts as the public, immutable ledger, recording hashes of vote metadata. This ensures transparency and prevents tampering with vote records.
3.  **IPFS (Interplanetary File System):** A decentralized storage system used to store the vote metadata itself. This provides data redundancy and prevents single points of failure.
4.  **Bitcoin RPC Client:** Used by the Flask application to interact with the Bitcoin Testnet (sending transactions).
5.  **IPFS Client:** Used by the Flask application to interact with the IPFS network (adding and retrieving metadata).

## Architecture Diagram

[Insert diagram here: `![Architecture Diagram](images/architecture_diagram.png)` - Place the diagram in the `docs/images` folder.]

(If you don't have a formal diagram you can describe it in text.) For example:

The Flask application handles user requests. When a user casts a vote, the application creates a JSON metadata object containing the voter and candidate IDs. This metadata is then added to IPFS, returning an IPFS hash (CID). The application then creates a Bitcoin transaction containing this IPFS hash in an `OP_RETURN` output and broadcasts it to the Bitcoin Testnet. Results are calculated by retrieving the stored IPFS hashes from the Bitcoin blockchain and subsequently retrieving the corresponding metadata from IPFS.

## Data Flow (Example: Casting a Vote)

1.  User submits a vote through the web interface.
2.  Flask application:
    *   Creates vote metadata (JSON).
    *   Uses `ipfs_utils` to add the metadata to IPFS.
    *   Receives the IPFS hash (CID).
    *   Constructs a Bitcoin transaction with the IPFS hash in `OP_RETURN`.
    * Uses the Bitcoin RPC client to send the transaction to the Bitcoin Testnet.
3. Bitcoin network confirms the transaction.
4. The transaction containing IPFS hash is recorded permanently in the blockchain