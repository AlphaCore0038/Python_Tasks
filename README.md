# Python Engineering Projects

A progressively structured portfolio of Python implementations spanning CLI tooling, data integration, web application development, cryptography, and algorithmic problem solving.

![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-3776AB?logo=python&logoColor=white)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-complete-brightgreen)
![Top language](https://img.shields.io/github/languages/top/AlphaCore0038/Python_Tasks)

## Overview

This repository is a collection of nine progressively complex Python implementations organized into three levels. Each project is self-contained, independently runnable, and demonstrates a distinct engineering concern rather than an isolated language feature.

The progression moves deliberately from computational fundamentals to application-level systems:

- **Core Python programming** — modular functions, control flow, exception handling, input validation
- **CLI application development** — interactive menus, stateful sessions, graceful termination
- **File processing** — text, JSON, and CSV handling through `pathlib`-based portable I/O
- **Persistent data management** - JSON document storage and relational persistence via SQLite
- **Web scraping** — HTTP retrieval and structured HTML parsing into tabular output
- **REST/API consumption** — request lifecycle management, JSON decoding, failure taxonomy
- **Web application development** — server-rendered interfaces backed by an ORM
- **Authentication and authorization** — registration, session login, password reset, role-scoped data visibility
- **Cryptographic file operations** — authenticated symmetric encryption with explicit key lifecycle handling
- **Backtracking algorithms** — constraint satisfaction over an explicit board state

Level 1 establishes computational foundations, Level 2 introduces external and persistent data, and Level 3 combines complete applications, security tooling, and algorithmic problem solving.

## Engineering Scope

| Domain | Technologies / Concepts |
|---|---|
| Core Python | Functions, control flow, exceptions, modules, `argparse` |
| CLI Engineering | Interactive menus, input validation, replay loops, exit codes |
| File Processing | `pathlib`, text processing, JSON, CSV |
| Web | Requests, BeautifulSoup, Django |
| APIs | HTTP GET, JSON parsing, status and failure handling |
| Security | Fernet symmetric encryption, token validation, key generation |
| Authentication | Django auth, password reset, role-based visibility |
| Algorithms | Backtracking, constraint satisfaction, board-state search |
| Persistence | JSON documents, SQLite via Django ORM |
| Testing | Django test suite, smoke testing, round-trip validation |

## Project Progression

```text
                          PYTHON ENGINEERING
                                    │
 ┌────────┼────────────────────────┼───────────────────────────┼─────────────┐
           │                        │                           │
     FUNDAMENTALS              INTEGRATION              ADVANCED SYSTEMS
           │                        │                           │
        Level 1                  Level 2                     Level 3
           │                        │                           │
 ┌──┼─────┼──────┼───┐      ┌──┼────┼────┼──┐      ┌───┼───────┼────────┼────┐
     │     │      │             │    │    │             │       │        │
   Calc  Guess  Files         Todo  Web  API         Django  Crypto  N-Queens
```

## Project Matrix

| Level | Project | Primary Technology | Engineering Focus |
|---|---|---|---|
| 1 | [Simple Calculator](Level-1-Basic/Task-1-Simple-Calculator/) | Python stdlib | Modular operations, input validation, exception flow |
| 1 | [Number Guessing Game](Level-1-Basic/Task-2-Number-Guessing-Game/) | `random` module | Randomized state, attempt lifecycle, control flow |
| 1 | [Word Counter](Level-1-Basic/Task-3-Word-Counter/) | `pathlib` | Filesystem interaction, text processing, error paths |
| 2 | [To-Do List Application](Level-2-Intermediate/Task-1-Todo-List-Application/) | JSON | Persistent state, CRUD operations, data integrity |
| 2 | [Web Scraper](Level-2-Intermediate/Task-2-Web-Scraper/) | Requests + BeautifulSoup | HTML parsing, structured extraction, CSV generation |
| 2 | [API Integration](Level-2-Intermediate/Task-3-API-Integration/) | Requests | HTTP client design, JSON decoding, failure handling |
| 3 | [Django Web Application](Level-3-Advanced/Task-1-Django-Web-Application/) | Django + SQLite | Authentication, authorization, ORM, server-rendered UI |
| 3 | [File Encryption/Decryption](Level-3-Advanced/Task-2-File-Encryption-Decryption/) | Cryptography (Fernet) | Key lifecycle, authenticated encryption pipeline |
| 3 | [N-Queens Solver](Level-3-Advanced/Task-3-N-Queens/) | Python stdlib | Backtracking search, constraint validation, board state |

## Level 1 — Computational Foundations

Level 1 isolates the core mechanics of well-structured procedural code: operations decomposed into **modular functions** with single responsibilities, **input validation** at every user-facing boundary, explicit **control flow** through menu-driven loops, and **exception handling** that separates error paths from the happy path instead of letting failures propagate. The guessing game exercises **randomized state** and bounded attempt lifecycles, while the word counter introduces **filesystem interaction** and **text processing** through `pathlib` with graceful handling of absent resources.

- [Simple Calculator](Level-1-Basic/Task-1-Simple-Calculator/) — four operations as discrete functions; division-by-zero and non-numeric input handling
- [Number Guessing Game](Level-1-Basic/Task-2-Number-Guessing-Game/) — `random.randint` range search with hints, attempt budget, replay loop
- [Word Counter](Level-1-Basic/Task-3-Word-Counter/) — file reading, whitespace tokenization, `FileNotFoundError` and I/O error paths

## Level 2 — Application & Data Integration

Level 2 marks the transition from isolated computations to applications that exchange data with the outside world. State outlives the process through **JSON persistence** with guarded load/save logic — including detection of corrupt storage rather than silent data loss. Networking is handled through **HTTP requests** with explicit timeouts and a classified error model (connection failure, timeout, HTTP status errors, malformed responses). Raw HTML is reduced to **structured records** through DOM parsing, and both scraped and consumed data are rendered into clean formats — **CSV generation** on one side, formatted **API response handling** on the other.

- [To-Do List Application](Level-2-Intermediate/Task-1-Todo-List-Application/) — CRUD lifecycle backed by a JSON document; invalid input and corrupted-file handling
- [Web Scraper](Level-2-Intermediate/Task-2-Web-Scraper/) — `requests` + `BeautifulSoup` extraction pipeline producing a typed CSV dataset
- [API Integration](Level-2-Intermediate/Task-3-API-Integration/) — REST client over JSONPlaceholder with response validation and id-based lookups

## Level 3 — Advanced Python Systems

### Django Web Application

A complete server-rendered task manager built on Django's authentication stack:

- **Authentication** — registration with hashed credential storage, session-based login/logout, and an email-driven **password reset** flow (console email backend for development)
- **Authorization and roles** — staff (admin) accounts observe global data; regular accounts are restricted to their own records at the query level
- **User-scoped data** — object access is scoped per request through the ORM, with 404 semantics for cross-user access attempts
- **CRUD operations** — create, read, update (including status toggling), and delete with confirmation flows
- **ORM / database layer** — Django models over SQLite with versioned migrations
- **Template-based interface** — base layout plus dedicated templates for auth flows and task views

→ [Django Web Application](Level-3-Advanced/Task-1-Django-Web-Application/)

### Cryptographic File Operations

- **Fernet symmetric encryption** — AES-128-CBC in an HMAC-SHA256 authenticated envelope
- **Key generation** — local `secret.key` creation on demand, never committed
- **Encryption/decryption pipeline** — file → ciphertext → byte-identical restoration
- **Invalid token handling** — wrong key or tampered ciphertext detected and reported without partial writes
- **Secure key handling** — key material excluded from version control; storage guidance documented

→ [File Encryption/Decryption](Level-3-Advanced/Task-2-File-Encryption-Decryption/)

### N-Queens Solver

- **Constraint satisfaction** — queens must not share row, column, or diagonal
- **Recursive backtracking** — place, recurse, undo on dead ends
- **Board-state representation** — explicit 2D array of `.` / `Q` cells
- **Diagonal and column validation** — pre-placement safety checks against all occupied rows
- **Configurable N** — supplied via argument or interactive prompt; unsolvable cases reported

→ [N-Queens Solver](Level-3-Advanced/Task-3-N-Queens/)

## Technology Stack

| Category | Components |
|---|---|
| **Language** | Python 3.12+ |
| **Web** | Django 6.1 |
| **HTTP / Data** | Requests, BeautifulSoup4, JSON, CSV |
| **Security** | Cryptography (Fernet) |
| **Database** | SQLite (via Django ORM) |
| **Algorithms** | Backtracking search |
| **Standard library** | `pathlib`, `argparse`, `random`, `json`, `csv` |

Each project declares its own `requirements.txt`; projects with no external dependencies document that explicitly.

## Repository Architecture

```text
.
├── README.md
├── LICENSE
├── .gitignore
│
├── Level-1-Basic/
│   ├── Task-1-Simple-Calculator/
│   │   ├── calculator.py
│   │   ├── README.md
│   │   └── requirements.txt
│   ├── Task-2-Number-Guessing-Game/
│   │   ├── game.py
│   │   ├── README.md
│   │   └── requirements.txt
│   └── Task-3-Word-Counter/
│       ├── word_counter.py
│       ├── sample.txt
│       ├── README.md
│       └── requirements.txt
│
├── Level-2-Intermediate/
│   ├── Task-1-Todo-List-Application/
│   │   ├── todo.py
│   │   ├── tasks.json
│   │   ├── README.md
│   │   └── requirements.txt
│   ├── Task-2-Web-Scraper/
│   │   ├── scraper.py
│   │   ├── data.csv
│   │   ├── README.md
│   │   └── requirements.txt
│   └── Task-3-API-Integration/
│       ├── api.py
│       ├── README.md
│       └── requirements.txt
│
└── Level-3-Advanced/
    ├── Task-1-Django-Web-Application/
    │   ├── manage.py
    │   ├── config/                 # Django project (settings, urls, wsgi, asgi)
    │   ├── tasks/                  # App: models, views, forms, urls, admin
    │   │   └── templates/          # base + auth + task templates
    │   ├── requirements.txt
    │   └── README.md
    ├── Task-2-File-Encryption-Decryption/
    │   ├── encrypt.py
    │   ├── decrypt.py
    │   ├── README.md
    │   └── requirements.txt
    └── Task-3-N-Queens/
        ├── n_queens.py
        ├── README.md
        └── requirements.txt
```

## Getting Started

### Clone

```bash
git clone https://github.com/AlphaCore0038/Python_Tasks.git
cd Python_Tasks
```

### Python environment

Requires **Python 3.12 or newer**.

```bash
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

```bash
# Linux / macOS
source .venv/bin/activate
```

### Dependencies

Dependencies are declared **per project** in each task's `requirements.txt`:

```bash
# Example: install dependencies for the web scraper
pip install -r Level-2-Intermediate/Task-2-Web-Scraper/requirements.txt
```

Level 1 projects, the To-Do application, and the N-Queens solver use only the standard library and require no installation.

## Running the Projects

```bash
# Level 1
python Level-1-Basic/Task-1-Simple-Calculator/calculator.py
python Level-1-Basic/Task-2-Number-Guessing-Game/game.py
python Level-1-Basic/Task-3-Word-Counter/word_counter.py

# Level 2
python Level-2-Intermediate/Task-1-Todo-List-Application/todo.py
python Level-2-Intermediate/Task-2-Web-Scraper/scraper.py        # needs network
python Level-2-Intermediate/Task-3-API-Integration/api.py        # needs network

# Level 3
cd Level-3-Advanced/Task-1-Django-Web-Application
python manage.py migrate
python manage.py runserver                                       # http://127.0.0.1:8000
python manage.py test                                            # test suite
cd ../..

python Level-3-Advanced/Task-2-File-Encryption-Decryption/encrypt.py <file>
python Level-3-Advanced/Task-2-File-Encryption-Decryption/decrypt.py <file>.enc
python Level-3-Advanced/Task-3-N-Queens/n_queens.py 8
```

Detailed instructions for each project live in its own `README.md`.

## Validation & Testing

The repository has been validated with the following checks:

- **Compilation checks** — `python -m compileall` across all three levels (syntax and import integrity)
- **CLI smoke testing** — scripted input runs exercising every menu path of the interactive programs
- **Error-path validation** — missing files, corrupted JSON storage, non-numeric input, out-of-range values, invalid menu selections, and non-zero exit codes
- **Scraper execution** — live retrieval and parsing against the target site, producing a verified CSV dataset
- **API request validation** — live requests covering the list, single-resource, and invalid-id paths
- **Django system checks and tests** — `manage.py check` plus a **9-test automated suite** covering registration, login redirects, password-reset email generation, per-role data visibility, CRUD operations, and cross-user access rejection
- **Encryption round-trip validation** — encrypt → decrypt compared byte-for-byte against the original, plus wrong-key and missing-file failure paths
- **N-Queens solution validation** — programmatically verified that produced boards contain N non-attacking queens across a range of N values, including unsolvable cases

## Engineering Characteristics

- **Modular implementation** — operations, persistence, scraping, and view logic separated into focused units
- **Explicit error handling** — typed exception handling with meaningful messages and meaningful exit codes
- **Portable filesystem paths** — `pathlib` with script-relative defaults; no hardcoded absolute paths
- **Minimal external dependencies** — four third-party packages across the entire repository
- **Separation of concerns** — models, forms, views, templates, and URL routing separated in the Django project
- **Reproducible setup** — per-project `requirements.txt` and documented migration steps
- **Secure handling of secrets** — keys and database files excluded from version control; secret key configurable via environment variable
- **Persistent data handling** — JSON document storage and SQLite with migrations
- **Algorithmic correctness** — solutions validated against explicit constraint checks

## Security Notes

- **No credentials are committed.** The repository contains no API keys, tokens, or passwords; external services used here are public and keyless.
- **Encryption keys are generated locally** (`secret.key`) and excluded from version control via `.gitignore` (`*.key`). Keys must be stored and backed up by the operator.
- **Django secret configuration** is overridable through the `DJANGO_SECRET_KEY` environment variable; the committed default is a development-only value.
- **`.gitignore` excludes sensitive and generated files**: `.env`, `*.key`, `db.sqlite3`, virtual environments, and `__pycache__` artifacts.
- **Passwords are hashed** by Django's authentication framework; plaintext credentials are never stored.

## Future Engineering Directions

The following are *possible future improvements* — none are implemented in the repository today:

- Automated test coverage beyond the Django test suite (pytest for CLI modules)
- CI validation workflow (linting, compilation checks, test execution)
- Containerized development environment
- Structured logging across projects
- Externalized configuration management
- Authenticated API access patterns
- Deployment automation

## License

This repository is released under the [MIT License](LICENSE).

Built as part of a Python internship and development program.
