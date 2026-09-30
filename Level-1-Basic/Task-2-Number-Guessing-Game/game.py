"""Number Guessing Game — guess a random number between 1 and 100.

Rules:
    * The computer picks a random number from 1 to 100.
    * The player has a limited number of attempts.
    * After every guess the game answers "Too high!" or "Too low!".
    * The game ends when the number is guessed or attempts run out.
    * The player may play again as many times as desired.
"""

from __future__ import annotations

import random

# Game configuration
LOW = 1
HIGH = 100
MAX_ATTEMPTS = 10


def get_guess(attempt: int) -> int:
    """Read and validate a single guess from the player.

    Keeps prompting until an integer within the game range is entered.
    """
    while True:
        raw = input(f"Attempt {attempt}/{MAX_ATTEMPTS} - Enter your guess ({LOW}-{HIGH}): ")
        try:
            guess = int(raw.strip())
        except ValueError:
            print("  Please enter a whole number.")
            continue
        if not LOW <= guess <= HIGH:
            print(f"  Out of range! Pick a number between {LOW} and {HIGH}.")
            continue
        return guess


def play_round() -> None:
    """Play one round of the guessing game."""
    secret = random.randint(LOW, HIGH)
    print(f"\nI am thinking of a number between {LOW} and {HIGH}.")

    for attempt in range(1, MAX_ATTEMPTS + 1):
        guess = get_guess(attempt)

        if guess > secret:
            print("  Too high! Try a smaller number.")
        elif guess < secret:
            print("  Too low! Try a larger number.")
        else:
            print(f"  Correct! You guessed it in {attempt} attempt(s).")
            return

        remaining = MAX_ATTEMPTS - attempt
        print(f"  Attempts remaining: {remaining}")

    print(f"  Game over! The number was {secret}.")


def main() -> None:
    """Run the game with a replay loop."""
    print("=" * 40)
    print("   NUMBER GUESSING GAME")
    print("=" * 40)

    while True:
        play_round()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again not in {"y", "yes"}:
            print("Thanks for playing. Goodbye!")
            break


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGame terminated. Goodbye!")
