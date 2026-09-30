"""API client for JSONPlaceholder — https://jsonplaceholder.typicode.com/users

A free fake REST API designed for testing and learning.

Usage:
    python api.py          # list all users
    python api.py 3        # show details of user with id 3

The JSON response is parsed and displayed as a clean, readable profile card.
Connection errors, timeouts, bad HTTP status codes and invalid JSON are all
handled with friendly messages.
"""

from __future__ import annotations

import json
import sys

import requests

API_URL = "https://jsonplaceholder.typicode.com/users"
REQUEST_TIMEOUT = 10  # seconds


def fetch_users() -> list[dict] | None:
    """Call the API and return the parsed list of users, or None on failure."""
    try:
        response = requests.get(API_URL, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()
    except requests.exceptions.Timeout:
        print(f"Error: the API did not respond within {REQUEST_TIMEOUT} seconds.")
        return None
    except requests.exceptions.HTTPError as exc:
        print(f"Error: API returned HTTP {exc.response.status_code}.")
        return None
    except requests.exceptions.ConnectionError:
        print("Error: could not reach the API. Check your internet connection.")
        return None
    except requests.exceptions.RequestException as exc:
        print(f"Error: unexpected request failure -> {exc}")
        return None

    # The status code was fine — but the body still might not be valid JSON.
    try:
        data = response.json()
    except (json.JSONDecodeError, requests.exceptions.JSONDecodeError):
        print("Error: API response is not valid JSON.")
        return None

    if not isinstance(data, list):
        print("Error: unexpected API response format (expected a list of users).")
        return None

    return data


def print_user(user: dict) -> None:
    """Print one user as a formatted profile card."""
    company = user.get("company") or {}
    address = user.get("address") or {}

    print(f"\n--- User #{user.get('id', '?')} " + "-" * 30)
    print(f"  Name    : {user.get('name', 'n/a')}")
    print(f"  Username: {user.get('username', 'n/a')}")
    print(f"  Email   : {user.get('email', 'n/a')}")
    print(f"  Phone   : {user.get('phone', 'n/a')}")
    print(f"  Website : {user.get('website', 'n/a')}")
    print(f"  Company : {company.get('name', 'n/a')} ({company.get('catchPhrase', 'n/a')})")
    print(f"  City    : {address.get('city', 'n/a')}")
    print("-" * 42)


def main(argv: list[str]) -> None:
    """Fetch users, then print all of them or a single one by id."""
    print(f"Calling {API_URL} ...")
    users = fetch_users()
    if users is None:
        sys.exit(1)

    # Optional: filter by id given on the command line.
    if len(argv) > 1:
        try:
            wanted = int(argv[1])
        except ValueError:
            print(f"Error: user id must be a number, got '{argv[1]}'.")
            sys.exit(1)

        match = next((u for u in users if u.get("id") == wanted), None)
        if match is None:
            print(f"No user found with id {wanted}. Valid ids: 1-{len(users)}.")
            sys.exit(1)

        print_user(match)
        return

    print(f"Fetched {len(users)} users. Showing all:")
    for user in users:
        print_user(user)


if __name__ == "__main__":
    try:
        main(sys.argv)
    except KeyboardInterrupt:
        print("\nRequest cancelled.")
        sys.exit(130)
