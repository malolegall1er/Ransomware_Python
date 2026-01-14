import json
import os

STORAGE_FILE = "clients.json"

def save_client(uuid, key):
    data = {}
    if os.path.exists(STORAGE_FILE):
        with open(STORAGE_FILE, "r") as f:
            data = json.load(f)
    data[uuid] = key
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)
