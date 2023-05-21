# Playing Cards
# Demonstrates combining objects
# 21/05/2023

class Card(object):
    """A playing card"""
    # Constants
    # Card Ranks
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    # Suits
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    # Return a string representation of a car
    def __str__(self):
        rep = self.rank + self.suit
        return rep
