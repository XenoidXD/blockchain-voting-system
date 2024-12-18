import hashlib
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException
from config import settings


class BitcoinTestnet:
    def __init__(self):
        """
        Initialize Bitcoin Testnet client using RPC credentials from settings.py.
        """
        self.rpc_url = f"http://{settings.RPC_USER}:{settings.RPC_PASSWORD}@{settings.BITCOIN_HOST}:{settings.BITCOIN_PORT}"
        try:
            self.client = AuthServiceProxy(self.rpc_url)
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Bitcoin Testnet: {str(e)}")

    def generate_new_address(self):
        """
        Generate a new Bitcoin address for receiving transactions.
        """
        try:
            return self.client.getnewaddress()
        except JSONRPCException as e:
            raise RuntimeError(f"Error generating new address: {e}")

    def get_balance(self):
        """
        Retrieve the wallet balance from the Bitcoin Testnet.
        """
        try:
            return self.client.getbalance()
        except JSONRPCException as e:
            raise RuntimeError(f"Error retrieving balance: {e}")

    def create_transaction(self, recipient_address, amount):
        """
        Create and send a transaction to a recipient address.
        """
        try:
            unspent = self.client.listunspent()
            inputs = []
            total_amount = 0

            # Gather UTXOs (Unspent Transaction Outputs)
            for utxo in unspent:
                inputs.append({
                    "txid": utxo['txid'],
                    "vout": utxo['vout']
                })
                total_amount += utxo['amount']
                if total_amount >= amount:
                    break

            if total_amount < amount:
                raise ValueError("Insufficient funds.")

            # Create transaction outputs
            outputs = {
                recipient_address: amount,
                self.client.getrawchangeaddress(): total_amount - amount - 0.0001  # Deduct fee
            }

            # Create, sign, and send transaction
            raw_tx = self.client.createrawtransaction(inputs, outputs)
            signed_tx = self.client.signrawtransactionwithwallet(raw_tx)
            txid = self.client.sendrawtransaction(signed_tx['hex'])
            return txid
        except JSONRPCException as e:
            raise RuntimeError(f"Error creating transaction: {e}")

    def store_metadata(self, metadata):
        """
        Store metadata on the Bitcoin Testnet using OP_RETURN output.
        """
        try:
            # Hash the metadata
            hashed_data = hashlib.sha256(metadata.encode()).hexdigest()

            # Gather UTXOs for creating a transaction
            unspent = self.client.listunspent()
            if not unspent:
                raise RuntimeError("No UTXOs available to create a transaction.")

            utxo = unspent[0]
            inputs = [{"txid": utxo["txid"], "vout": utxo["vout"]}]
            outputs = {}

            # Add OP_RETURN output with hashed metadata
            op_return_script = f"6a{len(hashed_data) // 2:02x}{hashed_data}"
            outputs["data"] = op_return_script

            # Include change output
            change_address = self.client.getrawchangeaddress()
            outputs[change_address] = utxo["amount"] - 0.0001  # Deduct fee

            # Create, sign, and broadcast the transaction
            raw_tx = self.client.createrawtransaction(inputs, outputs)
            signed_tx = self.client.signrawtransactionwithwallet(raw_tx)
            txid = self.client.sendrawtransaction(signed_tx["hex"])

            return {"txid": txid, "metadata_hash": hashed_data}
        except JSONRPCException as e:
            raise RuntimeError(f"Error storing metadata: {e}")
        except Exception as e:
            raise RuntimeError(f"Unexpected error: {e}")

    def verify_metadata(self, txid, expected_hash):
        """
        Verify if a transaction contains the expected metadata hash in its OP_RETURN output.
        """
        try:
            tx = self.client.getrawtransaction(txid, True)
            for vout in tx["vout"]:
                script_pub_key = vout["scriptPubKey"]
                if script_pub_key["type"] == "nulldata" and expected_hash in script_pub_key["asm"]:
                    return True
            return False
        except JSONRPCException as e:
            raise RuntimeError(f"Error verifying metadata: {e}")


if __name__ == "__main__":
    # Create an instance of the BitcoinTestnet class
    btc = BitcoinTestnet()

    print("Generating a new address:")
    new_address = btc.generate_new_address()
    print(f"New Address: {new_address}")

    print("Retrieving wallet balance:")
    balance = btc.get_balance()
    print(f"Wallet Balance: {balance} BTC")

    print("Storing metadata:")
    metadata = btc.store_metadata("Sample voting metadata")
    print(f"Transaction ID: {metadata['txid']}")
    print(f"Metadata Hash: {metadata['metadata_hash']}")

    print("Verifying metadata:")
    is_valid = btc.verify_metadata(metadata["txid"], metadata["metadata_hash"])
    print(f"Metadata valid: {is_valid}")
