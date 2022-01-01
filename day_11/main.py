############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
dealer_cards = []

start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print(logo)

def get_card(deck):
    deck.append(random.choice(cards))

def add_card(deck, ask_get_card):
    ask_get_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if ask_get_card == "y":
        get_card(deck)
    return ask_get_card


get_card(user_cards)
get_card(user_cards)
get_card(dealer_cards)
get_card(dealer_cards)

while start_game == "y":
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")
    start_game = add_card(user_cards, start_game)

print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
