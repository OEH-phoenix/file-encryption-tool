
import argparse
from cryptography.fernet import Fernet

# Load the key
def load_key(keyfile):
    with open(keyfile, "rb") as file:
        return file.read()

# Encrypt the file
def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted_data = f.encrypt(data)
    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    print(f"File {filename} encrypted.")

# Decrypt the file
def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filename.replace(".encrypted", ""), "wb") as file:
        file.write(decrypted_data)
    print(f"File {filename} decrypted.")

# Main function to handle the command-line arguments
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("action", help="encrypt or decrypt")
    parser.add_argument("filename", help="the file to encrypt or decrypt")
    parser.add_argument("keyfile", help="the key file to use")

    args = parser.parse_args()

    key = load_key(args.keyfile)

    if args.action == "encrypt":
        encrypt(args.filename, key)
    elif args.action == "decrypt":
        decrypt(args.filename, key)
