"""Command-line To-Do List application with permanent JSON storage.

Features:
    * View all tasks
    * Add a new task
    * Mark a task as completed
    * Delete a task
    * Automatic persistence in tasks.json (next to this script)

All operations validate user input and fail gracefully.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

# Storage file lives next to this script — no hardcoded absolute paths.
TASK_FILE = Path(__file__).with_name("tasks.json")


# ---------------------------------------------------------------------------
# Persistence
# ---------------------------------------------------------------------------
def load_tasks() -> list[dict]:
    """Load tasks from tasks.json.

    Returns an empty list when the file does not exist yet.

    Raises:
        SystemExit: if the file exists but contains invalid JSON
                    (so the file is never silently overwritten).
    """
    if not TASK_FILE.exists():
        return []

    try:
        data = json.loads(TASK_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        print(f"Error: {TASK_FILE.name} contains invalid JSON.")
        print("Fix or delete the file, then restart the app.")
        sys.exit(1)

    if not isinstance(data, list):
        print(f"Error: {TASK_FILE.name} has an unexpected format (expected a list).")
        sys.exit(1)

    return data


def save_tasks(tasks: list[dict]) -> None:
    """Write the task list back to tasks.json (pretty-printed)."""
    TASK_FILE.write_text(json.dumps(tasks, indent=2), encoding="utf-8")


# ---------------------------------------------------------------------------
# Operations
# ---------------------------------------------------------------------------
def view_tasks(tasks: list[dict]) -> None:
    """Print every task with its completion status."""
    if not tasks:
        print("\nNo tasks yet. Add one with option 2!")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "x" if task["done"] else " "
        print(f"  {task['id']}. [{status}] {task['title']}")
    print("------------------")


def add_task(tasks: list[dict]) -> list[dict]:
    """Prompt for a title and append a new task."""
    title = input("Enter task title: ").strip()
    if not title:
        print("  Task title cannot be empty.")
        return tasks

    next_id = max((task["id"] for task in tasks), default=0) + 1
    tasks.append({"id": next_id, "title": title, "done": False})
    print(f"  Added task #{next_id}: {title}")
    return tasks


def find_task(tasks: list[dict], prompt: str) -> dict | None:
    """Read a task id from the user and return the matching task (or None)."""
    raw = input(prompt).strip()
    try:
        task_id = int(raw)
    except ValueError:
        print("  Please enter a valid task number.")
        return None

    for task in tasks:
        if task["id"] == task_id:
            return task

    print(f"  No task found with id {task_id}.")
    return None


def complete_task(tasks: list[dict]) -> list[dict]:
    """Mark the selected task as completed."""
    task = find_task(tasks, "Enter task number to complete: ")
    if task is None:
        return tasks

    if task["done"]:
        print(f"  Task #{task['id']} is already completed.")
    else:
        task["done"] = True
        print(f"  Completed: {task['title']}")
    return tasks


def delete_task(tasks: list[dict]) -> list[dict]:
    """Remove the selected task from the list."""
    task = find_task(tasks, "Enter task number to delete: ")
    if task is None:
        return tasks

    tasks.remove(task)
    print(f"  Deleted: {task['title']}")
    return tasks


# ---------------------------------------------------------------------------
# Menu loop
# ---------------------------------------------------------------------------
def print_menu() -> None:
    """Display the main menu."""
    print("\n===== To-Do List =====")
    print("1. View tasks")
    print("2. Add task")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def main() -> None:
    """Run the interactive to-do menu until the user exits."""
    tasks = load_tasks()
    print("Welcome to the To-Do List App!")

    while True:
        print_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            tasks = add_task(tasks)
            save_tasks(tasks)
        elif choice == "3":
            tasks = complete_task(tasks)
            save_tasks(tasks)
        elif choice == "4":
            tasks = delete_task(tasks)
            save_tasks(tasks)
        elif choice == "5":
            print("Tasks saved. Goodbye!")
            break
        else:
            print("  Invalid option. Please enter a number from 1 to 5.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nApp terminated. Your tasks are safe in tasks.json.")
