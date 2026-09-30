"""Encrypt a file with Fernet symmetric encryption (AES-128-CBC + HMAC).

Usage:
    python encrypt.py --generate-key        # create secret.key (once)
    python encrypt.py <file>                # encrypt <file> -> <file>.enc

The key is stored next to this script as secret.key. If it does not exist,
it is generated automatically on the first encryption run.

KEY SAFETY: never share or commit secret.key — anyone holding it can decrypt
your files. (.gitignore already excludes *.key)
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from cryptography.fernet import Fernet

# Key lives next to this script — no hardcoded absolute paths.
KEY_FILE = Path(__file__).with_name("secret.key")


def generate_key(key_path: Path = KEY_FILE) -> bytes:
    """Create a new Fernet key and save it to key_path.

    Returns:
        The generated key (url-safe base64 bytes).
    """
    key = Fernet.generate_key()
    key_path.write_bytes(key)
    print(f"Key generated and saved to: {key_path.name}")
    print("Keep this file secret and never commit it to version control.")
    return key


def load_key(key_path: Path = KEY_FILE, create_if_missing: bool = True) -> bytes:
    """Load the Fernet key, generating one when the file is absent.

    Raises:
        SystemExit: if the key file cannot be read.
    """
    if not key_path.exists():
        if not create_if_missing:
            print(f"Error: key file not found -> {key_path.name}")
            print("Run: python encrypt.py --generate-key")
            sys.exit(1)
        print(f"Key file {key_path.name} not found — generating a new one.")
        return generate_key(key_path)

    key = key_path.read_bytes().strip()
    if not key:
        print(f"Error: {key_path.name} is empty. Delete it and generate a new key.")
        sys.exit(1)
    return key


def encrypt_file(input_path: Path, key: bytes) -> Path:
    """Encrypt input_path and write <name>.enc next to it.

    Raises:
        FileNotFoundError: if the input file does not exist.
        IsADirectoryError: if the input path is a directory.
        OSError: for any other read/write problem.
    """
    if not input_path.exists():
        raise FileNotFoundError(f"File not found: {input_path}")
    if input_path.is_dir():
        raise IsADirectoryError(f"Expected a file but got a directory: {input_path}")

    plain = input_path.read_bytes()
    encrypted = Fernet(key).encrypt(plain)

    output_path = input_path.with_name(input_path.name + ".enc")
    output_path.write_bytes(encrypted)
    return output_path


def main(argv: list[str] | None = None) -> None:
    """Parse CLI arguments and run the requested action."""
    parser = argparse.ArgumentParser(
        description="Encrypt a file using Fernet symmetric encryption."
    )
    parser.add_argument(
        "file", nargs="?", help="text file to encrypt (e.g. notes.txt)"
    )
    parser.add_argument(
        "--generate-key",
        action="store_true",
        help="generate a new secret.key and exit",
    )
    args = parser.parse_args(argv)

    if args.generate_key:
        generate_key()
        return

    if not args.file:
        parser.error("please provide a file to encrypt, or use --generate-key")

    input_path = Path(args.file)
    key = load_key()

    try:
        output_path = encrypt_file(input_path, key)
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    except IsADirectoryError as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    except OSError as exc:
        print(f"Error: could not read or write the file -> {exc}")
        sys.exit(1)

    original_size = input_path.stat().st_size
    encrypted_size = output_path.stat().st_size
    print(f"Encrypted: {input_path.name} -> {output_path.name}")
    print(f"Size: {original_size} bytes -> {encrypted_size} bytes")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled.")
        sys.exit(130)
