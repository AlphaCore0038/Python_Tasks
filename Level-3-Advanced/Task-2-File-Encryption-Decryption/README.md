# File Encryption / Decryption

## Description

A command-line tool that encrypts and decrypts text files using **Fernet**
symmetric encryption (from the `cryptography` library) — AES-128-CBC in an
HMAC-SHA256 authenticated envelope. The same key encrypts and decrypts, and
tampering or a wrong key is detected immediately.

## Features

- **Key generation** (`--generate-key`, or automatic on first encryption)
- Encrypt any file → `<name>.enc` (e.g. `notes.txt` → `notes.txt.enc`)
- Decrypt back to the exact original file (byte-for-byte round-trip)
- Handles missing files, missing/empty keys and invalid tokens (wrong key or
  tampered data) with clear messages and non-zero exit codes
- No hardcoded paths — key and files resolve relative to where you run it

## Requirements

- Python 3.12+
- `cryptography` (see `requirements.txt`)

## Installation

```bash
cd Level-3-Advanced/Task-2-File-Encryption-Decryption
python -m venv .venv
# Windows: .venv\Scripts\activate   |   macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## How to Run

```bash
# 1. (Optional) generate a key — otherwise one is created automatically
python encrypt.py --generate-key

# 2. Encrypt a file
python encrypt.py notes.txt          # creates notes.txt.enc

# 3. Decrypt it back
python decrypt.py notes.txt.enc      # restores notes.txt
```

### Key storage instructions

- The key is stored as `secret.key` next to the scripts.
- **Treat it like a password**: anyone with the key can read your files.
- Never commit it — `.gitignore` already excludes `*.key`.
- Back it up somewhere safe (password manager, offline copy). **Losing the key
  means losing access to the encrypted files permanently.**
- Use a different key per sensitive dataset; rotate by re-encrypting with a
  new key.

## Example Output

```
$ python encrypt.py --generate-key
Key generated and saved to: secret.key
Keep this file secret and never commit it to version control.

$ python encrypt.py notes.txt
Encrypted: notes.txt -> notes.txt.enc
Size: 39 bytes -> 140 bytes

$ python decrypt.py notes.txt.enc
Decrypted: notes.txt.enc -> notes.txt
Original content restored successfully.
```

Wrong key:

```
Error: invalid key or corrupted data — decryption failed.
Make sure you are using the same secret.key that encrypted this file.
```
