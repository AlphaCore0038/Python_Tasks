"""Simple Calculator — command-line calculator for basic arithmetic.

Operations:
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division

The program runs in a loop until the user chooses to exit.
Invalid numbers and division by zero are handled gracefully.
"""

from __future__ import annotations

from collections.abc import Callable

# ---------------------------------------------------------------------------
# Operation functions
# ---------------------------------------------------------------------------
def add(a: float, b: float) -> float:
    """Return the sum of a and b."""
    return a + b


def subtract(a: float, b: float) -> float:
    """Return the difference of a and b."""
    return a - b


def multiply(a: float, b: float) -> float:
    """Return the product of a and b."""
    return a * b


def divide(a: float, b: float) -> float:
    """Return a divided by b.

    Raises:
        ZeroDivisionError: if b is zero.
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


# Mapping of menu choice -> (label, function)
OPERATIONS: dict[str, tuple[str, Callable[[float, float], float]]] = {
    "1": ("Addition", add),
    "2": ("Subtraction", subtract),
    "3": ("Multiplication", multiply),
    "4": ("Division", divide),
}


# ---------------------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------------------
def read_number(prompt: str) -> float:
    """Prompt the user until a valid number is entered."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("  Invalid input. Please enter a numeric value.")


def read_choice() -> str:
    """Prompt the user until a valid menu choice is entered."""
    valid = set(OPERATIONS) | {"5"}
    while True:
        choice = input("Choose an operation (1-5): ").strip()
        if choice in valid:
            return choice
        print("  Invalid choice. Please enter a number from 1 to 5.")


# ---------------------------------------------------------------------------
# Main loop
# ---------------------------------------------------------------------------
def print_menu() -> None:
    """Display the calculator menu."""
    print("\n===== Simple Calculator =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")


def main() -> None:
    """Run the interactive calculator loop."""
    print("Welcome to the Simple Calculator!")

    while True:
        print_menu()
        choice = read_choice()

        if choice == "5":
            print("Goodbye!")
            break

        label, operation = OPERATIONS[choice]
        a = read_number("Enter first number:  ")
        b = read_number("Enter second number: ")

        try:
            result = operation(a, b)
        except ZeroDivisionError as exc:
            print(f"  Error: {exc}")
            continue

        print(f"  {label}: {a:g} and {b:g} = {result:g}")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram terminated. Goodbye!")
