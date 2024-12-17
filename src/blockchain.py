import hashlib
import requests
from bitcoinrpc.authproxy import AuthServiceProxy, JSONRPCException

class BitcoinTestnet:
    def __init__(self, rpc_user, rpc_password, host="127.0.0.1", port=18332):
        self.rpc_url = f"http://{rpc_user}:{rpc_password}@{host}:{port}"
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

    def create_transaction(self, sender_address, recipient_address, amount):
        """
        Create and send a transaction from the sender address to recipient address.
        """
        try:
            unspent = self.client.listunspent()
            inputs = []
            total_amount = 0

            # Gather UTXOs (Unspent Transaction Outputs)
            for utxo in unspent:
                if utxo['address'] == sender_address:
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
                sender_address: total_amount - amount - 0.0001  # Deduct fee
            }

            # Create, sign, and send transaction
            raw_tx = self.client.createrawtransaction(inputs, outputs)
            signed_tx = self.client.signrawtransactionwithwallet(raw_tx)
            txid = self.client.sendrawtransaction(signed_tx['hex'])
            return txid
        except JSONRPCException as e:
            raise RuntimeError(f"Error creating transaction: {e}")

    def store_metadata(self, data):
        """
        Store metadata on the Bitcoin Testnet using OP_RETURN output.
        """
        try:
            # Hash the data
            hashed_data = hashlib.sha256(data.encode()).hexdigest()

            # Create a raw transaction with OP_RETURN
            op_return_script = f"6a{len(hashed_data) // 2:02x}{hashed_data}"
            new_address = self.generate_new_address()

            txid = self.create_transaction(
                sender_address=new_address,
                recipient_address="1BitcoinEaterAddressDontSendf59kuE",
                amount=0.0001  # Minimal dust amount
            )

            return {
                "txid": txid,
                "metadata_hash": hashed_data
            }
        except Exception as e:
            raise RuntimeError(f"Error storing metadata: {e}")

if __name__ == "__main__":
    rpc_user = "your_rpc_user"
    rpc_password = "your_rpc_password"

    btc = BitcoinTestnet(rpc_user, rpc_password)

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
