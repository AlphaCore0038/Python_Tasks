# N-Queens Solver

## Description

A classic backtracking solver for the **N-Queens problem**: place N queens on
an N x N chessboard so that no two queens share a row, column or diagonal.
The board is represented as a 2D array and printed with a clear border.

## Features

- Backtracking algorithm with explicit `is_safe` position validation
- Board represented as a 2D list (`.` empty / `Q` queen)
- Configurable N — pass it on the command line or be prompted
- Detects the impossible cases (N = 2 and N = 3)
- Input validation (integers ≥ 1 only, argparse errors for junk input)
- Exit code 0 when a solution is found, 1 when none exists

## Requirements

- Python 3.12+
- No external libraries (standard library only)

## Installation

No installation needed:

```bash
cd Level-3-Advanced/Task-3-N-Queens
python n_queens.py
```

## How to Run

```bash
# Option 1: pass N directly
python n_queens.py 8

# Option 2: interactive prompt
python n_queens.py
Enter the value of N (board size): 5
```

## Example Output

```
$ python n_queens.py 4
Solving the 4-Queens problem ...

Solution found:

+---+---+---+---+
| . | Q | . | . |
+---+---+---+---+
| . | . | . | Q |
+---+---+---+---+
| Q | . | . | . |
+---+---+---+---+
| . | . | Q | . |
+---+---+---+---+
```

No solution:

```
$ python n_queens.py 2
Solving the 2-Queens problem ...

No solution exists for N = 2.
(The N-Queens problem has no solution when N = 2 or N = 3.)
```
