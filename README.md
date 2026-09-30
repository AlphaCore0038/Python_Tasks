# Codveda Python Development Internship — Python_Tasks

A complete collection of projects built during the **Codveda Python Development Internship**.
Every task is an independent, runnable project organised across three difficulty levels.

## Internship Details

| | |
|---|---|
| **Program** | Codveda Python Development Internship |
| **Language** | Python 3.12+ (developed on Python 3.14) |
| **Levels** | 3 levels × 3 tasks = **9 projects** |
| **License** | MIT |

## Completed Tasks

### Level 1 — Basic
| # | Task | Description |
|---|------|-------------|
| 1 | [Simple Calculator](Level-1-Basic/Task-1-Simple-Calculator/) | CLI calculator with add/subtract/multiply/divide and error handling |
| 2 | [Number Guessing Game](Level-1-Basic/Task-2-Number-Guessing-Game/) | Guess a random number (1–100) with hints and attempt limits |
| 3 | [Word Counter](Level-1-Basic/Task-3-Word-Counter/) | Count words in a text file with missing-file handling |

### Level 2 — Intermediate
| # | Task | Description |
|---|------|-------------|
| 1 | [To-Do List Application](Level-2-Intermediate/Task-1-Todo-List-Application/) | CLI task manager with permanent JSON storage |
| 2 | [Web Scraper](Level-2-Intermediate/Task-2-Web-Scraper/) | Scrape quotes from a website and save them to CSV |
| 3 | [API Integration](Level-2-Intermediate/Task-3-API-Integration/) | Consume a public REST API and display formatted data |

### Level 3 — Advanced
| # | Task | Description |
|---|------|-------------|
| 1 | [Django Web Application](Level-3-Advanced/Task-1-Django-Web-Application/) | Task manager with registration, login, password reset and roles |
| 2 | [File Encryption/Decryption](Level-3-Advanced/Task-2-File-Encryption-Decryption/) | Fernet-based file encryption with key generation |
| 3 | [N-Queens Solver](Level-3-Advanced/Task-3-N-Queens/) | Backtracking solver on a 2D board with configurable N |

## Technologies Used

- **Language:** Python 3.12+
- **Standard library:** `random`, `csv`, `json`, `pathlib`, `argparse`
- **External libraries:** `requests`, `beautifulsoup4`, `cryptography`, `Django`
- **Database:** SQLite (Django default)

## Repository Structure

```
Codveda-Python-Internship/
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
    │   ├── config/            # Django project (settings, urls)
    │   ├── tasks/             # Task manager app
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

## How to Run

Each task folder is independently runnable. General pattern:

```bash
# 1. Enter the task folder
cd Level-1-Basic/Task-1-Simple-Calculator

# 2. (If the task has dependencies) create a virtual environment
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS/Linux
pip install -r requirements.txt

# 3. Run the script
python calculator.py
```

### Quick command reference

```bash
# Level 1
python Level-1-Basic/Task-1-Simple-Calculator/calculator.py
python Level-1-Basic/Task-2-Number-Guessing-Game/game.py
python Level-1-Basic/Task-3-Word-Counter/word_counter.py

# Level 2
python Level-2-Intermediate/Task-1-Todo-List-Application/todo.py
python Level-2-Intermediate/Task-2-Web-Scraper/scraper.py
python Level-2-Intermediate/Task-3-API-Integration/api.py

# Level 3
cd Level-3-Advanced/Task-1-Django-Web-Application
python manage.py migrate && python manage.py runserver
python Level-3-Advanced/Task-2-File-Encryption-Decryption/encrypt.py
python Level-3-Advanced/Task-3-N-Queens/n_queens.py
```

> Full per-task instructions live in each task's `README.md`.

## License

This repository is licensed under the [MIT License](LICENSE).
