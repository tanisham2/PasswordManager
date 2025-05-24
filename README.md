## 🔐 Blockchain-based Password Manager
A lightweight command-line password manager secured with blockchain integrity and Fernet encryption. Each password entry is stored in an immutable blockchain, ensuring tamper-proof storage.

## ✨ Features
- 🔒 Secure password storage with Fernet symmetric encryption
- ⛓️ Blockchain-based structure to ensure integrity
- 🧠 Simple CLI to add, view, and verify passwords
- 📁 Stores data in data/blockchain.json
- 🔐 Uses getpass for secure password input

## 🛠️ Technologies
1. Python 3
2. JSON file storage
3. Cryptography (Fernet encryption)
4. Custom blockchain structure


##  📦 Project Structure
PasswordManager_Proj/
├── main.py               # CLI logic and main menu
├── blockchain.py         # Blockchain and Block class
├── crypto.py             # Encryption/decryption helpers
├── data/
│   └── blockchain.json   # Encrypted password blockchain
└── README.md

## 🚀 Getting Started
1) Clone the repo : 
git clone https://github.com/yourusername/password-manager-blockchain.git
cd password-manager-blockchain

2) Install dependencies
pip install cryptography

3) Run the app
python main.py

## 🧪 Commands
Add Password – Encrypts and adds a new site login

View Passwords – Decrypts and shows all saved logins

Verify Blockchain Integrity – Confirms no tampering

## ⚠️ Disclaimer
This is a learning project, not recommended for storing real credentials. For real-world password storage, use a dedicated tool like Bitwarden or KeePass.
