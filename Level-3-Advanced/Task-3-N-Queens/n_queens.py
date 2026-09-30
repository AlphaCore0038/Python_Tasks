"""N-Queens solver using the backtracking algorithm.

The N-Queens problem: place N queens on an N x N chessboard so that no two
queens attack each other (no shared row, column or diagonal).

Usage:
    python n_queens.py        # prompts for N
    python n_queens.py 8      # solve for N = 8 directly

The board is represented as a 2D list of "." (empty) and "Q" (queen).
"""

from __future__ import annotations

import argparse
import sys

# Type alias: a board is a 2D list of single-character strings.
Board = list[list[str]]


def new_board(n: int) -> Board:
    """Create an empty n x n board filled with '.' cells."""
    return [["." for _ in range(n)] for _ in range(n)]


def is_safe(board: Board, row: int, col: int) -> bool:
    """Check whether a queen placed at (row, col) attacks no other queen.

    Scans the same column and both diagonals. Rows above `row` are the only
    ones already occupied (queens are placed one row at a time).
    """
    n = len(board)

    # Same column
    for r in range(row):
        if board[r][col] == "Q":
            return False

    # Upper-left diagonal
    r, c = row - 1, col - 1
    while r >= 0 and c >= 0:
        if board[r][c] == "Q":
            return False
        r, c = r - 1, c - 1

    # Upper-right diagonal
    r, c = row - 1, col + 1
    while r >= 0 and c < n:
        if board[r][c] == "Q":
            return False
        r, c = r - 1, c + 1

    return True


def solve(board: Board, row: int = 0) -> bool:
    """Fill the board row by row using backtracking.

    Returns:
        True when all queens are placed (a solution is on the board),
        False when the current branch leads to a dead end.
    """
    n = len(board)

    if row == n:  # every row has a queen -> solution found
        return True

    for col in range(n):
        if is_safe(board, row, col):
            board[row][col] = "Q"          # place queen
            if solve(board, row + 1):       # try to solve the rest
                return True
            board[row][col] = "."          # backtrack: remove queen

    return False  # no column works for this row -> trigger backtracking


def print_board(board: Board) -> None:
    """Print the board with a simple border for clear reading."""
    n = len(board)
    border = "+" + "---+" * n

    print(border)
    for row in board:
        print("| " + " | ".join(row) + " |")
        print(border)


def solve_and_display(n: int) -> int:
    """Solve for n queens, print the result, and return the exit code."""
    print(f"Solving the {n}-Queens problem ...\n")
    board = new_board(n)

    if solve(board):
        print("Solution found:\n")
        print_board(board)
        return 0

    print(f"No solution exists for N = {n}.")
    print("(The N-Queens problem has no solution when N = 2 or N = 3.)")
    return 1


def read_n_interactive() -> int:
    """Prompt the user for a valid board size."""
    while True:
        raw = input("Enter the value of N (board size): ").strip()
        try:
            n = int(raw)
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if n < 1:
            print("  N must be 1 or greater.")
            continue
        return n


def main(argv: list[str] | None = None) -> int:
    """Parse CLI arguments and run the solver."""
    parser = argparse.ArgumentParser(
        description="Solve the N-Queens problem with backtracking."
    )
    parser.add_argument(
        "n",
        nargs="?",
        type=int,
        help="board size N (e.g. 8). Omit to be prompted.",
    )
    args = parser.parse_args(argv)

    if args.n is None:
        n = read_n_interactive()
    elif args.n < 1:
        parser.error("N must be 1 or greater")
    else:
        n = args.n

    return solve_and_display(n)


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, EOFError):
        print("\nCancelled.")
        sys.exit(130)
