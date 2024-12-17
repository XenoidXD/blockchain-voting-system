# Blockchain Voting System

## Description
The **Blockchain Voting System** is a prototype application designed to ensure transparency and security in the voting process using blockchain technology. By leveraging Bitcoin Testnet and IPFS for distributed data storage, this system provides anonymity for voters, real-time result updates, and an immutable record of votes stored on the blockchain.

## Features
- **Anonymous Voting**: Voters can cast their votes without revealing their identity, secured through cryptography.
- **Real-Time Results**: Results are displayed in real-time, ensuring transparency.
- **Blockchain Record**: Votes and metadata are securely stored in the Bitcoin Testnet blockchain and IPFS.
- **Tamper-Proof**: Immutable records guarantee the integrity of the election process.

## Technology Stack
- **Backend**: Python (Flask framework)
- **Blockchain**: Bitcoin Testnet
- **Distributed Storage**: IPFS
- **Cryptography**: SHA-256 hashing

## Installation
### Prerequisites
- Python 3.8 or later
- Bitcoin Core with Testnet enabled
- IPFS client

### Steps
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/blockchain-voting-system.git
   cd blockchain-voting-system
   ```

2. **Install Dependencies**
   Use pip to install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Bitcoin RPC**
   Update the `BITCOIN_RPC_USER`, `BITCOIN_RPC_PASSWORD`, `BITCOIN_RPC_HOST`, and `BITCOIN_RPC_PORT` values in the script to match your Bitcoin Core setup.

4. **Run the Application**
   Start the Flask server:
   ```bash
   python app.py
   ```

5. **Access the Application**
   Open your browser and navigate to `http://127.0.0.1:5000`.

## API Endpoints
### 1. **Register Candidate**
   - **Endpoint**: `/register_candidate`
   - **Method**: POST
   - **Payload**:
     ```json
     {
       "name": "Candidate Name"
     }
     ```
   - **Response**:
     ```json
     {
       "message": "Candidate registered successfully.",
       "id": "candidate_id"
     }
     ```

### 2. **Vote**
   - **Endpoint**: `/vote`
   - **Method**: POST
   - **Payload**:
     ```json
     {
       "voter_id": "unique_voter_identifier",
       "candidate_id": "candidate_id"
     }
     ```
   - **Response**:
     ```json
     {
       "message": "Vote recorded successfully.",
       "txid": "transaction_id",
       "ipfs_hash": "ipfs_hash"
     }
     ```

### 3. **Get Results**
   - **Endpoint**: `/results`
   - **Method**: GET
   - **Response**:
     ```json
     {
       "tally": {
         "Candidate Name": 5
       },
       "total_votes": 10,
       "blockchain_records": [
         {
           "ipfs_hash": "hash_value",
           "txid": "transaction_id"
         }
       ]
     }
     ```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contribution
Contributions are welcome! Feel free to fork the repository and submit a pull request with your enhancements.

## Contact
For any inquiries, reach out via email at [incxenoid@gmail.com](mailto:incxenoid@gmail.com).

