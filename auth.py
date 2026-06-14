import hashlib
import json
import os

PIN_FILE = "pin.json"

def hash_pin(pin):
    return hashlib.sha256(pin.encode()).hexdigest()

def setup_pin(pin):
    if not os.path.exists(PIN_FILE):
        with open(PIN_FILE, "w") as f:
            json.dump({"pin": hash_pin(pin)}, f)
        return True
    return False

def verify_pin(pin):
    if not os.path.exists(PIN_FILE):
        return False

    with open(PIN_FILE, "r") as f:
        data = json.load(f)

    return data["pin"] == hash_pin(pin)
