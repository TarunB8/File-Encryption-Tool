from cryptography.fernet import Fernet

# Load the key from file
def load_key():
    return open("secret.key", "rb").read()

# Encrypt the file
def encrypt_file(file_path):
    key = load_key()
    f = Fernet(key)

    with open(file_path, "rb") as file:
        original_data = file.read()

    encrypted_data = f.encrypt(original_data)

    with open(file_path + ".enc", "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)

    print(f"🔒 {file_path} encrypted successfully!")

# Decrypt the file
def decrypt_file(encrypted_path, output_path):
    key = load_key()
    f = Fernet(key)

    with open(encrypted_path, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(output_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"🔓 {encrypted_path} decrypted successfully into {output_path}")
