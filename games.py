# Games Module
# demonstrates Module creation
# 23/05/2023

class Player():
    """ A player for a game. """

    def __init__(self, name, score=0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = f"{self.name}:\t {str(self.score)}"

# create functions


def ask_yes_no(question):
    """Ask a yes or no question"""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response


def ask_number(question, low, high):
    """Ask for a number within a range"""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response


if __name__ == "__main__":
    print("This module needs to be imported and not ran directly")
    input("\n\nPress enter to exit the program.")
