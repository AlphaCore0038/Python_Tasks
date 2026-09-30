# To-Do List Application

## Description

A command-line to-do manager that stores tasks permanently in a JSON file.
Add, view, complete and delete tasks — everything persists between runs in
`tasks.json`.

## Features

- View tasks with completion status (`[ ]` pending / `[x]` done)
- Add tasks (empty titles rejected)
- Mark tasks as completed (idempotent)
- Delete tasks by id
- Permanent JSON storage (`tasks.json`, created next to the script)
- Input validation for menu choices and task ids
- Corrupt/invalid JSON is detected and never silently overwritten

## Requirements

- Python 3.12+
- No external libraries (standard library only)

## Installation

No installation needed:

```bash
cd Level-2-Intermediate/Task-1-Todo-List-Application
python todo.py
```

## How to Run

```bash
python todo.py
```

Pick an option from the menu (1–5). Changes are saved to `tasks.json`
automatically after every modification.

## Example Output

```
Welcome to the To-Do List App!

===== To-Do List =====
1. View tasks
2. Add task
3. Mark task as completed
4. Delete task
5. Exit
Choose an option (1-5): 2
Enter task title: Finish internship report
  Added task #1: Finish internship report

Choose an option (1-5): 1

--- Your Tasks ---
  1. [ ] Finish internship report
------------------

Choose an option (1-5): 3
Enter task number to complete: 1
  Completed: Finish internship report

Choose an option (1-5): 5
Tasks saved. Goodbye!
```

`tasks.json` after the session:

```json
[
  {
    "id": 1,
    "title": "Finish internship report",
    "done": true
  }
]
```
