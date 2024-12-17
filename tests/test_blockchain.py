# Test for blockchain logic
# Example enhanced tests, adapt as needed based on your blockchain implementation.
import pytest
from blockchain import Blockchain, Block            # Import your blockchain and block classes

def test_create_blockchain():
    """Tests the creation of a new blockchain."""
    bc = Blockchain()
    assert len(bc.chain) == 1                       # starts with genesis block
    assert bc.chain[0].previous_hash == "0"         # genesis block's previous hash
    assert bc.chain[0].data == "Genesis Block"      # genesis data

def test_add_block():
    """Tests adding a new block to the blockchain."""
    bc = Blockchain()
    bc.add_block("Test Data 1")
    assert len(bc.chain) == 2
    assert bc.chain[1].data == "Test Data 1"
    assert bc.chain[1].previous_hash == bc.chain[0].hash

def test_is_chain_valid():
   bc = Blockchain()
   bc.add_block("test data")
   assert bc.is_chain_valid() == True

   #Manipulate a block to make chain invalid
   bc.chain[1].data = "tampered data"
   assert bc.is_chain_valid() == False