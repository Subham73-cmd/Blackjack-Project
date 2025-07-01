# Blackjack Game in Python

Welcome to the **Blackjack Game**! This is a simple, interactive command-line implementation of the classic card game Blackjack, written in Python. The game allows you to play against the computer, simulating the basic rules and flow of Blackjack.

## Features

- Play against a computer dealer.
- Handles Blackjack (Ace + 10) and bust scenarios.
- Simple user input for "hit" or "stand".
- Automatic dealer logic.
- Replay option after each game.

## How to Play

- Run the script.
- You and the computer are each dealt two cards.
- Try to get as close to 21 as possible without going over.
- Type `'y'` to get another card ("hit") or `'n'` to pass ("stand").
- The computer will draw according to simple dealer rules.
- The winner is determined based on standard Blackjack rules.

## Getting Started

### Prerequisites

- Python 3.x installed on your machine.

### Running the Game

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Subham73-cmd/blackjack-python.git
    cd blackjack-python
    ```

2. **Run the script:**
    ```bash
    python blackjack.py
    ```

## Code Overview

The main functions in the script are:

- `card_deck()`: Returns a random card from the deck.
- `calculate_score(cards)`: Calculates the score for a hand.
- `compare(u_score, c_score)`: Compares user and computer scores to determine the outcome.
- `play_game()`: Orchestrates the flow of the game.

## Example Gameplay

```
Your card: [8, 10], your score: 18
Computer's first cards: 7
Type 'y' to get another card or type 'n' to pass: n
Final hand is [8, 10], final score is 18
Computer's final hand [7, 10, 5], final score 22
Opponent went over. You win
Do you want to play blackjack game ? Type 'y' for yes or 'n' for no
```

## Notes

- This is a basic version for educational purposes.

## Author

- [Subham Nayak](https://github.com/Subham73-cmd)

Enjoy playing Blackjack! 🃏
