# Number Guessing Game

## Description

A classic guessing game where the computer picks a random number between
1 and 100 and the player tries to find it. The game gives high/low hints
after every attempt and ends when the number is guessed or attempts run out.

## Features

- Random number generated with Python's `random` module (1–100)
- Configurable maximum attempts (default: 10)
- "Too high!" / "Too low!" hints after each guess
- Input validation (integers only, inside range)
- Replay option after every round

## Requirements

- Python 3.12+
- No external libraries (standard library only)

## Installation

No installation needed:

```bash
cd Level-1-Basic/Task-2-Number-Guessing-Game
python game.py
```

## How to Run

```bash
python game.py
```

Enter your guess when prompted. Answer `y` to play again or anything else
to quit.

## Example Output

```
========================================
   NUMBER GUESSING GAME
========================================

I am thinking of a number between 1 and 100.
Attempt 1/10 — Enter your guess (1-100): 50
  Too low! Try a larger number.
  Attempts remaining: 9
Attempt 2/10 — Enter your guess (1-100): 75
  Too high! Try a smaller number.
  Attempts remaining: 8
Attempt 3/10 — Enter your guess (1-100): 63
  Correct! You guessed it in 3 attempt(s).

Play again? (y/n): n
Thanks for playing. Goodbye!
```
