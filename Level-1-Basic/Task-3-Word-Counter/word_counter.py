"""Word Counter — count the number of words in a text file.

Usage:
    python word_counter.py               # counts words in bundled sample.txt
    python word_counter.py path/to/file  # counts words in your own file

Handles missing files gracefully and reports the result in a clean format.
"""

from __future__ import annotations

import sys
from pathlib import Path

# Default file bundled next to this script
DEFAULT_FILE = Path(__file__).with_name("sample.txt")


def count_words(path: Path) -> int:
    """Return the number of whitespace-separated words in the file.

    Raises:
        FileNotFoundError: if the file does not exist.
        OSError: if the file cannot be read.
    """
    text = path.read_text(encoding="utf-8")
    return len(text.split())


def main(argv: list[str]) -> None:
    """Parse the command-line argument, count words and print the result."""
    # Command-line argument wins, otherwise use the bundled sample file.
    target = Path(argv[1]) if len(argv) > 1 else DEFAULT_FILE

    print(f"Word Counter\nFile: {target}")

    try:
        word_count = count_words(target)
    except FileNotFoundError:
        print(f"Error: File not found -> {target}")
        print("Tip: pass an existing file, e.g. python word_counter.py sample.txt")
        sys.exit(1)
    except OSError as exc:
        print(f"Error: Could not read the file -> {exc}")
        sys.exit(1)

    print(f"Total words: {word_count}")


if __name__ == "__main__":
    main(sys.argv)
