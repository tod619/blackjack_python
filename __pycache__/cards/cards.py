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

# Create a hand class which is a collection of card objects


class Hand(object):
    """A hand of playing cards"""

    def __init__(self) -> None:
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<empty>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)
