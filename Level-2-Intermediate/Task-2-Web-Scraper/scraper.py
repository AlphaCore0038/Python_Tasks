"""Web scraper for https://quotes.toscrape.com — saves quotes into data.csv.

The target site is a public sandbox built specifically for scraping practice.

For every quote on the first page the scraper extracts:
    * the quote text
    * the author
    * comma-separated tags

Results are written to data.csv (created/overwritten next to this script).
Connection problems, timeouts and HTTP errors are reported clearly.
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://quotes.toscrape.com"
OUTPUT_FILE = Path(__file__).with_name("data.csv")
REQUEST_TIMEOUT = 10  # seconds

# A normal browser-like User-Agent is polite and avoids needless 403s.
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; CodvedaInternshipBot/1.0)"}


def fetch_page(url: str) -> BeautifulSoup | None:
    """Fetch a URL and return a BeautifulSoup document, or None on failure."""
    try:
        response = requests.get(url, headers=HEADERS, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print(f"Error: request to {url} timed out after {REQUEST_TIMEOUT}s.")
        return None
    except requests.exceptions.HTTPError as exc:
        print(f"Error: server responded with {exc.response.status_code} for {url}.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: could not connect. Check your internet connection.")
        return None
    except requests.exceptions.RequestException as exc:
        print(f"Error: unexpected request failure -> {exc}")
        return None

    return BeautifulSoup(response.text, "html.parser")


def scrape_quotes(soup: BeautifulSoup) -> list[dict]:
    """Extract (text, author, tags) for every quote on the page."""
    quotes = []
    for block in soup.select("div.quote"):
        text = block.select_one("span.text")
        author = block.select_one("small.author")
        tags = block.select("a.tag")

        if not (text and author):
            continue  # skip malformed entries instead of crashing

        quotes.append(
            {
                "quote": text.get_text(strip=True),
                "author": author.get_text(strip=True),
                "tags": ", ".join(tag.get_text(strip=True) for tag in tags),
            }
        )
    return quotes


def save_to_csv(quotes: list[dict], path: Path) -> None:
    """Write the scraped quotes to a CSV file."""
    with path.open("w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["quote", "author", "tags"])
        writer.writeheader()
        writer.writerows(quotes)


def main() -> None:
    """Run the scraper: fetch -> parse -> save."""
    print(f"Scraping {BASE_URL} ...")
    soup = fetch_page(BASE_URL)
    if soup is None:
        sys.exit(1)

    quotes = scrape_quotes(soup)
    if not quotes:
        print("Error: no quotes found — the page structure may have changed.")
        sys.exit(1)

    save_to_csv(quotes, OUTPUT_FILE)
    print(f"Saved {len(quotes)} quotes to {OUTPUT_FILE.name}")
    print("\nFirst quote:")
    print(f'  "{quotes[0]["quote"]}" — {quotes[0]["author"]}')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nScrape cancelled.")
        sys.exit(130)
