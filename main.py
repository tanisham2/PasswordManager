import json
import os
import getpass
from blockchain import Blockchain
from crypto import encrypt_password, decrypt_password

DATA_FILE = 'data/blockchain.json'  
                                          # Ensure data directory exists
if not os.path.exists('data'):
    os.makedirs('data')

# Load blockchain
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'r') as f:
        blockchain_data = json.load(f)            
        blockchain = Blockchain.from_list(blockchain_data)
else:
    blockchain = Blockchain()

def save_blockchain():
    with open(DATA_FILE, 'w') as f:                
        json.dump(blockchain.to_list(), f, indent=4)

def add_password():
    site = input("Enter website: ")
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ") 
    
    entry_data = {'site': site, 'username': username, 'password': encrypt_password(password)}
    blockchain.add_block(entry_data)
    save_blockchain()
    print("Password added securely!")

def view_passwords():
    for block in blockchain.chain[1:]:  # Skip genesis
        data = block.data
        try:
            password = decrypt_password(data['password'])
            print(f"[{block.index}] {data['site']} | {data['username']} | {password}")
        except Exception:
            print(f"[{block.index}] Encrypted/corrupt data")

def verify_integrity():
    if blockchain.is_chain_valid():
        print("Blockchain integrity: ✅ Valid")
    else:
        print("Blockchain integrity: ❌ Broken")

def main():
    while True:
        print("\n--- Password Manager ---")
        print("1. Add Password")
        print("2. View Passwords")
        print("3. Verify Blockchain Integrity")
        print("4. Exit")
        choice = input("Choice: ")

        if choice == '1':
            add_password()
        elif choice == '2':
            view_passwords()
        elif choice == '3':
            verify_integrity()
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == '__main__':
    main()
