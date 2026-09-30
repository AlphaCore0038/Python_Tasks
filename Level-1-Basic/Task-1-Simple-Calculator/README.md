# Simple Calculator

## Description

A beginner-friendly command-line calculator that performs basic arithmetic
operations — addition, subtraction, multiplication and division. Each operation
is implemented as its own function, and the program validates all user input.

## Features

- Four operations: addition, subtraction, multiplication, division
- Separate reusable function per operation
- Interactive menu loop (exit any time)
- Division-by-zero error handling
- Non-numeric input handling
- Clean, readable CLI output

## Requirements

- Python 3.12+
- No external libraries (standard library only)

## Installation

No installation needed — clone the repository and run the script:

```bash
cd Level-1-Basic/Task-1-Simple-Calculator
python calculator.py
```

## How to Run

```bash
python calculator.py
```

Choose an operation (1–4), enter two numbers, and the result is printed.
Choose `5` to exit.

## Example Output

```
Welcome to the Simple Calculator!

===== Simple Calculator =====
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exit
Choose an operation (1-5): 1
Enter first number:  12
Enter second number: 8
  Addition: 12 and 8 = 20

===== Simple Calculator =====
...
Choose an operation (1-5): 4
Enter first number:  10
Enter second number: 0
  Error: Cannot divide by zero.

Choose an operation (1-5): 5
Goodbye!
```
