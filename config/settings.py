# config/settings.py
import json
import os

try:
    with open("config/credentials.json", "r") as f:
        CREDENTIALS = json.load(f)
except FileNotFoundError:
    print("Error: config/credentials.json not found. Create it from credentials.template.json")
    exit(1)
except json.JSONDecodeError:
    print("Error: Invalid JSON in config/credentials.json")
    exit(1)

RPC_USER = CREDENTIALS.get("bitcoin_rpc_user")
RPC_PASSWORD = CREDENTIALS.get("bitcoin_rpc_password")
IPFS_HTTP_API = CREDENTIALS.get("ipfs_http_api")

# Konfigurasi tambahan (jika diperlukan)
FLASK_PORT = int(os.getenv("FLASK_PORT", 5000))
FLASK_HOST = os.getenv("FLASK_HOST", "127.0.0.1")
DEBUG = bool(os.getenv("DEBUG", True))
IPFS_GATEWAY = os.getenv("IPFS_GATEWAY", "https://ipfs.io/ipfs/") # Contoh IPFS gateway

if not RPC_USER or not RPC_PASSWORD:
    raise ValueError("Bitcoin RPC credentials (user and password) are missing in credentials.json")

if not IPFS_HTTP_API:
  raise ValueError("IPFS API Address are missing in credentials.json")