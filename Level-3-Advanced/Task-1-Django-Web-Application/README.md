# Django Task Manager (Web Application)

## Description

A full-stack task manager built with **Django**. Users register, log in and
manage their own tasks through a clean web UI. Admins see everyone's tasks
and get access to the Django admin site. Password reset works out of the box
using Django's console email backend, so no SMTP account is needed for
development.

## Features

- User **registration** (auto-login after sign-up)
- **Login / logout** (Django's built-in authentication)
- **Password reset** by email (reset link printed to the runserver terminal)
- Secure password handling (Django's `UserCreationForm` + password validators,
  hashed storage — plain passwords are never stored)
- **User roles**
  - **Admin** (`is_staff`): sees all tasks + full `/admin/` site
  - **Regular user**: sees and manages only their own tasks
- Task CRUD: create, view, **update status** (quick toggle + edit form), delete
- Persistent storage in **SQLite** (`db.sqlite3`, auto-created)
- Responsive UI with no external CSS/JS
- 9 automated tests (`python manage.py test`)

## Requirements

- Python 3.12+
- Django 6.1+ (see `requirements.txt`)
- No other external dependencies

## Installation

```bash
cd Level-3-Advanced/Task-1-Django-Web-Application

# 1. Create and activate a virtual environment
python -m venv .venv
# Windows:      .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure the database (creates db.sqlite3 and applies migrations)
python manage.py migrate

# 4. (Optional) create an admin account for the admin role
python manage.py createsuperuser
```

### Database configuration

The project ships with Django's default **SQLite** configuration
(`config/settings.py` → `DATABASES`), which needs zero setup: `migrate`
creates `db.sqlite3` next to `manage.py`. To use another database (PostgreSQL,
MySQL, ...), replace the `DATABASES` dictionary in `config/settings.py` with
your engine, name, user and password, then run `python manage.py migrate`
again. The database file is git-ignored.

### Email (password reset) configuration

Development uses Django's **console email backend**: the password-reset link
is printed in the `runserver` terminal. For production, point `MAILERS` in
`config/settings.py` at a real SMTP service and set credentials via environment
variables — never commit secrets.

## How to Run

```bash
python manage.py runserver
```

Then open <http://127.0.0.1:8000/> in your browser.

| URL | Purpose |
|-----|---------|
| `/` | Task list (login required) |
| `/register/` | Create an account |
| `/accounts/login/` | Log in |
| `/accounts/logout/` | Log out (POST) |
| `/accounts/password_reset/` | Reset password |
| `/admin/` | Django admin (superuser only) |
| `/tasks/new/`, `/tasks/<id>/edit/`, `/tasks/<id>/toggle/`, `/tasks/<id>/delete/` | Task CRUD |

### Useful commands

```bash
python manage.py runserver      # start the development server
python manage.py test           # run the automated test suite
python manage.py check          # validate the project
python manage.py createsuperuser  # create an admin-role account
```

## Example Output

Registering, then viewing tasks:

```
Welcome, alice! Your account was created.

My Tasks
3 total · 2 pending · 1 completed

[ ] Finish internship report      PENDING    [Done] [Edit] [Delete]
[x] Buy groceries                 DONE       [Undo] [Edit] [Delete]
```

Password reset (printed in the runserver terminal):

```
Content-Type: text/plain; charset="utf-8"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit
Subject: Password reset on 127.0.0.1:8000
From: webmaster@localhost
To: alice@example.com

Hello alice,

Someone requested a password reset for your Task Manager account.
Follow the link below to choose a new password:

http://127.0.0.1:8000/accounts/reset/MQ/dfr1oq-11042e6673b5dd7198cfd4f3b9d660b3/
```

Running the test suite:

```
Found 9 test(s).
...
----------------------------------------------------------------------
Ran 9 tests in 21.1s

OK
```
