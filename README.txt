
# Simple File Encryption Tool

This project contains two Python scripts for basic file encryption and decryption using symmetric encryption with the `cryptography` library (`Fernet`).

## Files

1. **generate_key.py**: Generates a symmetric encryption key and saves it to a file.
2. **crypto_tool.py**: Encrypts and decrypts files using a symmetric key.

## Requirements

- Python 3.x
- cryptography library

To install the cryptography library, run:

```bash
pip install cryptography
```

## Usage

### 1. Generate an encryption key

Run the `generate_key.py` script to generate a symmetric key:

```bash
python generate_key.py
```

This will create a file called `key.key` in the same directory, which contains the encryption key.

### 2. Encrypt a file

Use the `crypto_tool.py` script to encrypt a file:

```bash
python crypto_tool.py encrypt <filename> <keyfile>
```

Example:

```bash
python crypto_tool.py encrypt secret.txt key.key
```

This will generate an encrypted file called `secret.txt.encrypted`.

### 3. Decrypt a file

To decrypt a file, use the same key file that was used for encryption:

```bash
python crypto_tool.py decrypt <filename.encrypted> <keyfile>
```

Example:

```bash
python crypto_tool.py decrypt secret.txt.encrypted key.key
```

This will decrypt the file and restore it to its original state.

## Notes

- Make sure to securely store the `key.key` file, as it's required for both encryption and decryption.
- If you lose the key, the encrypted files cannot be decrypted.
