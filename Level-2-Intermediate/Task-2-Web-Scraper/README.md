# Web Scraper

## Description

A beginner-friendly web scraper that extracts quotes, authors and tags from
[quotes.toscrape.com](https://quotes.toscrape.com) — a public sandbox site
built specifically for scraping practice — and saves the results to `data.csv`.

## Features

- Fetches pages with `requests` (10 s timeout, polite User-Agent)
- Parses HTML with `BeautifulSoup`
- Extracts quote text, author and tags
- Writes results to CSV (`data.csv`, next to the script)
- Clear error handling for connection failures, timeouts and HTTP errors
- Skips malformed entries instead of crashing

## Requirements

- Python 3.12+
- `requests`, `beautifulsoup4` (see `requirements.txt`)
- Internet connection

## Installation

```bash
cd Level-2-Intermediate/Task-2-Web-Scraper
python -m venv .venv
# Windows: .venv\Scripts\activate   |   macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## How to Run

```bash
python scraper.py
```

The script overwrites `data.csv` on every successful run. A pre-generated
sample `data.csv` is included in this folder.

## Example Output

```
Scraping https://quotes.toscrape.com ...
Saved 10 quotes to data.csv

First quote:
  "The world as we have created it is a process of our thinking..." — Albert Einstein
```

Connection problem:

```
Scraping https://quotes.toscrape.com ...
Error: could not connect. Check your internet connection.
```
