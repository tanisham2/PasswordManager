from cryptography.fernet import Fernet
                                                # You can use a saved key or generate a new one and store it securely
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

def encrypt_password(password: str) -> str:
    return cipher.encrypt(password.encode()).decode()

def decrypt_password(token: str) -> str:
    return cipher.decrypt(token.encode()).decode()
