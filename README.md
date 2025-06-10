# 🔐 File Encryption Tool using Python

## 🧾 Project Description
This is a simple but effective File Encryption Tool built using **Python** and the **Cryptography** library. It encrypts and decrypts files using symmetric encryption (Fernet), keeping your sensitive data safe and secure.

---

## 🚀 Features
- Generate secure encryption keys
- Encrypt any text file using AES-based Fernet encryption
- Decrypt encrypted files using the saved key
- Very beginner-friendly and Pythonic!

---

## 📁 Folder Structure
File-Encryption-Tool/
├── generate_key.py # Generates encryption key
├── file_encryptor.py # Contains encrypt/decrypt logic
├── run_encrypt.py # Encrypts a sample file
├── run_decrypt.py # Decrypts back to original
├── sample.txt # Original input file
├── secret.key # Auto-generated encryption key
├── sample.txt.enc # Encrypted file
├── output.txt # Decrypted result
└── screenshots/ # Output images for proof

---

## 🧪 How to Run
1. Install Python
2. Install the required library:
   ```bash
   pip install cryptography

Generate encryption key (run once):
python generate_key.py
Encrypt file: python run_encrypt.py
Decrypt file: python run_decrypt.py

🙌 Developed by
Puttamraju Sai Tarun
Engineering Student | Cyber Security Enthusiast
