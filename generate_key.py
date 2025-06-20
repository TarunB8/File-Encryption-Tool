from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Save the key into a file
with open("secret.key", "wb") as key_file:
    key_file.write(key)

print("✅ Key generated and saved as secret.key")
