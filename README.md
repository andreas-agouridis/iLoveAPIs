# iLoveAPIs 🔐

iLoveAPIs is a simple and secure Python desktop app for storing and testing APIs.

You can save:

* API Name
* API URL / Endpoint
* API Key / Token

All saved APIs are encrypted and protected behind a PIN login.

---

# Features

- PIN protection

- Encrypted API storage

- Add unlimited APIs

- Store API name, endpoint URL, and API key

- Test API button

- Clean desktop UI

---

# Project Structure

```txt
iLoveAPIs/
│── main.py          # Main application UI
│── auth.py          # PIN authentication
│── storage.py       # Encrypted storage + API testing
│── apis.enc         # Encrypted APIs file
│── secret.key       # Encryption key
│── pin.json         # Saved hashed PIN
```

---

# Requirements

Install Python 3.10+ recommended.

Install dependencies:

```bash
pip install cryptography requests
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/andreas-agouridis/iLoveAPIs.git
```

Go to the project folder:

```bash
cd iLoveAPIs
```

Install dependencies:

```bash
pip install cryptography requests
```

Run the app:

```bash
python main.py
```

---

# How It Works

### First Launch

When opening the app for the first time:

1. Enter a new PIN
2. The app saves a hashed version of your PIN
3. Your encrypted API vault is created

### Login

On future launches:

* Enter your PIN
* Access your saved APIs

### Add API

Fill in:

* API Name
* API URL
* API Key (optional)

Press **Add API** to save it.

### Test API

Select an API and press **Test API**.

The app will:

* Send a request to the API endpoint
* Check if the API responds
* Display:

  * Success ✅
  * Failure ❌
  * Status code

Example:

```txt
API Works (200)
```

or

```txt
Failed (404)
```

---

# Security

iLoveAPIs stores APIs in encrypted form.

Current security includes:

* PIN-protected login
* SHA-256 PIN hashing
* Encrypted API database

### Important Note

The current version stores an encryption key locally (`secret.key`).

For stronger security, future versions should derive the encryption key directly from the PIN so data becomes impossible to decrypt without the correct PIN.

Because secrets lying around on disk is how developers accidentally invent drama.

---

# Technologies Used

* Python
* Tkinter
* Requests
* Cryptography (Fernet)

---

# Future Improvements

* Edit API entries
* Delete APIs
* Dark mode
* PIN change
* Search APIs
* Export / Import encrypted backups
* Better encryption tied to PIN
* Custom headers for API testing

---

# License

MIT License

Feel free to modify and improve the project.
