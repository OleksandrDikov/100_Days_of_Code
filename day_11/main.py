from art import logo
import random


def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def add_card(deck, ask_get_card):
    ask_get_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if ask_get_card == "y":
        deck.append(deal_card())
    return ask_get_card

def choose_winner(user_deck, dealer_deck):
    if user_deck == 21 or user_deck > dealer_deck or dealer_deck > 21:
        print("You win!")
    elif user_deck == dealer_deck:
        print("Draw!")
    else:
        print("You lose!")


user_cards = []
dealer_cards = []
start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
print(logo)

for _ in random(2):
    user_cards.append(deal_card())
    dealer_cards.append(deal_card())

while start_game == "y":
    if sum(user_cards) > 21:
        print("You lose!")
        break
    print(f"Your cards: {user_cards}, current score: {sum(user_cards)}")
    print(f"Dealer's first card: {dealer_cards[0]}")
    start_game = add_card(user_cards, start_game)

while sum(dealer_cards) < 14:
    dealer_cards.append(deal_card())

print(f"Your final hand: {user_cards}, final score: {sum(user_cards)}")
print(f"Computer's final hand: {dealer_cards}, final score: {sum(dealer_cards)}")
choose_winner(sum(user_cards), sum(dealer_cards))
