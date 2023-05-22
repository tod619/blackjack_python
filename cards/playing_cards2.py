# Playing Cards Version 2.0
# Demonstrates inheritance - class extensions
# 22/05/2023

# Create a Card Object
class Card():
    """A Playing Card Object"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["\u2663", "\u2665", "\u2666", "\u2660"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = f"{self.rank}:{self.suit}"
        return rep

# Unprintable card inherits from Card class


class Unprintable_Card(Card):
    """A card that won't reveal its roan or suit when printed"""

    def __str__(self):
        return "<unprintable>"

# Card flipping class  inherits from Card class


class Flippable_Card(Card):
    """A Card that can be face up or face down"""

    def __init__(self, rank, suit, face_up=True):
        super(Flippable_Card, self).__init__(rank, suit)
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = super(Flippable_Card, self).__str__()
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up


class Hand():
    """A hand of playing cards"""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += f"{str(card)} \t"
        else:
            rep = "<EMPTY>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

# Create a deck class that inherits from the Hand class


class Deck(Hand):
    """A Deck of playing cards"""

    def create_deck(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't deal any more. Out of cards!")


card1 = Card(Card.RANKS[1], Card.SUITS[3])
card2 = Card(Card.RANKS[1], Card.SUITS[0])
card3 = Card(Card.RANKS[0], Card.SUITS[3])
card4 = Card(Card.RANKS[11], Card.SUITS[1])
card5 = Card(Card.RANKS[9], Card.SUITS[2])
print(card1)

my_hand = Hand()
my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)

# print(my_hand)

deck1 = Deck()
deck1.create_deck()
# print(deck1)
deck1.shuffle()
# print(deck1)

# Create an unprintable card and print it
card6 = Unprintable_Card(Card.RANKS[0], Card.SUITS[1])
print(card6)

card7 = Flippable_Card(Card.RANKS[0], Card.SUITS[0])
# print card7 face up
print(card7)  # A of Clubs
# flip card7 and print it
card7.flip()
print(card7)
# flip it back to face up
card7.flip()
print(card7)

input("\nPress enter to exit the program ")
