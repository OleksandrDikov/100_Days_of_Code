import os
from art import logo


def clear_console():
    os.system('clear')


play = True
player_list = {}

while play:
    clear_console()
    print(logo)
    user_name = input("What is your name?: ")
    user_bid = int(input("What is your bid?: $"))
    next_player = input("Are there any other bidders? Type 'yes or 'no'.\n")
    player_list[user_name] = user_bid
    if next_player != "yes":
        play = False

max_bid = max(player_list, key=player_list.get)
clear_console()
print(f"The winner is {max_bid} with a bid of ${player_list[max_bid]}")
