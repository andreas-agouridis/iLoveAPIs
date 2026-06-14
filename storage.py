import json
import os
import requests
from cryptography.fernet import Fernet
import hashlib

FILE = "apis.enc"

def make_key(pin):
    hashed = hashlib.sha256(pin.encode()).digest()
    return hashed[:32].hex().encode()[:44]

def encrypt_data(data, pin):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    encrypted = cipher.encrypt(json.dumps(data).encode())

    with open("secret.key", "wb") as f:
        f.write(key)

    return encrypted

def decrypt_data(data):
    with open("secret.key", "rb") as f:
        key = f.read()

    cipher = Fernet(key)
    return json.loads(cipher.decrypt(data).decode())

def load_apis(pin):
    if not os.path.exists(FILE):
        return []

    with open(FILE, "rb") as f:
        encrypted = f.read()

    try:
        return decrypt_data(encrypted)
    except:
        return []

def save_api(api, pin):
    apis = load_apis(pin)
    apis.append(api)

    encrypted = encrypt_data(apis, pin)

    with open(FILE, "wb") as f:
        f.write(encrypted)

def test_api(url):
    try:
        response = requests.get(url, timeout=5)
        return response.ok, response.status_code
    except Exception as e:
        return False, str(e)
