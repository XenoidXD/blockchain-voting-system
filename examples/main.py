from flask import Flask, request, jsonify
from blockchain import BitcoinTestnet
from ipfs_utils import IPFSClient
import hashlib
import os

app = Flask(__name__)