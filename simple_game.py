# Simple game
# demonstrates importing modules
# 23/05/2023

import games
import random

print("Wlecom to the world's simplest game. \n")

again = None

while again != "n":
    players = []

    num = games.ask_number(
        question="How many players? (2 - 5): ", low=2, high=5)

    for i in range(num):
        name = input("Player Name: ")
        score = random.randrange(100) + 1
        player = games.Player(name, score)
        players.append(player)

    print("\nHere are the game results:")
    for player in players:
        print(player)
    again = games.ask_yes_no("\nDo you wnat to play again? (y/n): ")

input("\n\nPress the enter key to exit")
