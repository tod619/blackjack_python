# Playing Cards Version 2.0
# Demonstrates inheritance - class extensions
# 22/05/2023

# Create a Card Object
class Card():
    """A Playing Card Object"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["\u2663", "\u2665", "\u2666", "\u2660"]

    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        rep = f"{self.rank}:{self.suit}"
        return rep


card1 = Card(Card.RANKS[1], Card.SUITS[3])
print(card1)

input("\nPress enter to exit the program")
