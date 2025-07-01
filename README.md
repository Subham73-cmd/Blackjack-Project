This is a simple console-based Blackjack game implemented in Python. The user plays against the computer (dealer) in an attempt to get as close to 21 as possible without going over. The game includes the standard Blackjack rules like dealing cards, score calculation, and Ace value adjustment.


Features
Play a simplified version of Blackjack.
Random card dealing from a standard Blackjack deck.
Ace (11) value automatically adjusts to 1 if the total exceeds 21.
Blackjack detection for an instant win (21 with two cards).
Automatic dealer behavior (draws until score ≥ 17).
Score comparison with game outcome display.

Prerequisites
Python 3.x installed on your system.

How to Play
You and the computer are each dealt two cards.

The goal is to get a score as close to 21 as possible without exceeding it.

Cards 2-10 are worth their number; face cards are worth 10; Ace can be 11 or 1.

If your score is over 21, you lose.

You can choose to take another card or pass.

The computer (dealer) draws until their score is 17 or higher.

The highest score ≤ 21 wins. A Blackjack (21 with 2 cards) beats any other score.
