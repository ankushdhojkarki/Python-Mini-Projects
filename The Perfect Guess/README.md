# 🎯 Perfect Guess – A Number Guessing Game in Python

This is a simple terminal-based number guessing game built using Python. The game generates a random number between 1 and 100, and the user tries to guess it. It tracks the number of guesses and maintains a high score using a `highscore.txt` file.

## 📌 How It Works

- The program generates a random number between 1 and 100.
- The user is prompted to guess the number until they guess it correctly.
- After each wrong guess, the program tells the user to guess a smaller or larger number.
- The total number of guesses is counted.
- If the number of guesses is less than the current high score stored in `highscore.txt`, it updates the high score.

## 📁 Files Included

- `ThePerfectGuess.py` — The main game script.
- `highscore.txt` — Stores the current high score (minimum number of guesses).

## ▶️ How to Run

1. Make sure you have Python installed.
2. Place both `ThePerfectGuess.py` and `highscore.txt` in the same folder.
3. Open your terminal or command prompt.
4. Run the game using:

```bash
python ThePerfectGuess.py
