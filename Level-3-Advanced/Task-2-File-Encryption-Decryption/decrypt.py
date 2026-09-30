"""Decrypt a Fernet-encrypted file back to its original contents.

Usage:
    python decrypt.py <file.enc>            # restores the original file

Requires the same secret.key that was used for encryption.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from cryptography.fernet import Fernet, InvalidToken

# Key lives next to this script — no hardcoded absolute paths.
KEY_FILE = Path(__file__).with_name("secret.key")


def load_key(key_path: Path = KEY_FILE) -> bytes:
    """Load the Fernet key needed for decryption.

    Raises:
        SystemExit: if the key file is missing or empty.
    """
    if not key_path.exists():
        print(f"Error: key file not found -> {key_path.name}")
        print("Decryption requires the same key used for encryption.")
        sys.exit(1)

    key = key_path.read_bytes().strip()
    if not key:
        print(f"Error: {key_path.name} is empty — cannot decrypt.")
        sys.exit(1)
    return key


def decrypt_file(enc_path: Path, key: bytes) -> Path:
    """Decrypt enc_path and restore the original file.

    The output name has the trailing `.enc` removed (notes.txt.enc -> notes.txt).

    Raises:
        FileNotFoundError: if the encrypted file does not exist.
        InvalidToken: if the key is wrong or the data was tampered with.
        OSError: for any other read/write problem.
    """
    if not enc_path.exists():
        raise FileNotFoundError(f"File not found: {enc_path}")
    if enc_path.is_dir():
        raise IsADirectoryError(f"Expected a file but got a directory: {enc_path}")

    decrypted = Fernet(key).decrypt(enc_path.read_bytes())

    name = enc_path.name
    output_name = name[: -len(".enc")] if name.endswith(".enc") else name + ".dec"
    output_path = enc_path.with_name(output_name)
    output_path.write_bytes(decrypted)
    return output_path


def main(argv: list[str] | None = None) -> None:
    """Parse CLI arguments and run decryption."""
    parser = argparse.ArgumentParser(
        description="Decrypt a Fernet-encrypted file back to its original contents."
    )
    parser.add_argument("file", help="encrypted file to decrypt (e.g. notes.txt.enc)")
    args = parser.parse_args(argv)

    enc_path = Path(args.file)
    key = load_key()

    try:
        output_path = decrypt_file(enc_path, key)
    except FileNotFoundError as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    except IsADirectoryError as exc:
        print(f"Error: {exc}")
        sys.exit(1)
    except InvalidToken:
        print("Error: invalid key or corrupted data — decryption failed.")
        print("Make sure you are using the same secret.key that encrypted this file.")
        sys.exit(1)
    except OSError as exc:
        print(f"Error: could not read or write the file -> {exc}")
        sys.exit(1)

    print(f"Decrypted: {enc_path.name} -> {output_path.name}")
    print("Original content restored successfully.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nCancelled.")
        sys.exit(130)
