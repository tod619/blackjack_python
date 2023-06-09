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
                rep += f"{str(card)}  "
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

# create a hand object and print it
my_hand = Hand()
print("\nPrinting my_hand before I give it anny cards: ")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nPrinting my-hand after adding 5 cards: ")
print(my_hand)

# Create your_hand object
your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("Deal the first 2 cards from my hand to your hand")
print("Your Hand: ")
print(your_hand)
print("My Hand:")
print(my_hand)

# Clear my hand
my_hand.clear()
print("My hand after clearing it")
print(my_hand)
input("Press enter to exit!")
