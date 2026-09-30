# API Integration

## Description

A REST API client that consumes the free
[JSONPlaceholder](https://jsonplaceholder.typicode.com/users) user endpoint,
parses the JSON response and displays each user as a clean profile card.

## Features

- Calls a public API with `requests`
- Parses JSON responses
- Formatted, readable output (name, email, company, city, ...)
- Optional filter: show a single user by id (`python api.py 3`)
- Handles connection errors, timeouts, HTTP errors, invalid JSON and
  unexpected response shapes

## Requirements

- Python 3.12+
- `requests` (see `requirements.txt`)
- Internet connection

## Installation

```bash
cd Level-2-Intermediate/Task-3-API-Integration
python -m venv .venv
# Windows: .venv\Scripts\activate   |   macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
```

## How to Run

```bash
# Show all 10 users
python api.py

# Show a single user
python api.py 3
```

## Example Output

```
Calling https://jsonplaceholder.typicode.com/users ...
Fetched 10 users. Showing all:

--- User #1 ------------------------------
  Name    : Leanne Graham
  Username: Bret
  Email   : Sincere@april.biz
  Phone   : 1-770-736-8031 x56442
  Website : hildegard.org
  Company : Romaguera-Crona (Multi-layered/client-server intranet)
  City    : Gwenborough
------------------------------------------
```

Error handling:

```
Error: could not reach the API. Check your internet connection.
```
