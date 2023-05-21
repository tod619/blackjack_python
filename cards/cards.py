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


# main
card1 = Card(rank="A", suit="c")
print("Printing a card object")
print(card1)

# Creating more cards + printing them
card2 = Card(rank="2", suit="c")
card3 = Card(rank="3", suit="c")
card4 = Card(rank="4", suit="c")
card5 = Card(rank="5", suit="c")

print(card2)
print(card3)
print(card4)
print(card5)
