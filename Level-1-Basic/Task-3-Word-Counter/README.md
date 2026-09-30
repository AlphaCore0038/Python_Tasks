# Word Counter

## Description

A small command-line tool that reads a text file and reports how many words
it contains. A bundled `sample.txt` is included so the program works out of
the box, and missing files are reported with a friendly error.

## Features

- Reads any UTF-8 text file
- Counts whitespace-separated words
- Default file: `sample.txt` (bundled with the task)
- Custom file via command-line argument
- Handles `FileNotFoundError` and read errors gracefully

## Requirements

- Python 3.12+
- No external libraries (standard library only)

## Installation

No installation needed:

```bash
cd Level-1-Basic/Task-3-Word-Counter
python word_counter.py
```

## How to Run

```bash
# Count words in the bundled sample
python word_counter.py

# Count words in your own file
python word_counter.py path/to/your/file.txt
```

## Example Output

```
Word Counter
File: C:\...\sample.txt
Total words: 101
```

Missing file:

```
Word Counter
File: does_not_exist.txt
Error: File not found -> does_not_exist.txt
Tip: pass an existing file, e.g. python word_counter.py sample.txt
```
