import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_list = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
random_choice = random.randint(0, 2)

print(game_list[user_choice])
print("Computer chose:")
print(game_list[random_choice])

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
elif user_choice == random_choice:
    print("It's a draw")
elif (user_choice == 0 and random_choice == 1) or (user_choice == 1 and random_choice == 2) \
        or (user_choice == 2 and random_choice == 0):
    print("Yuo lose!")
else:
    print("You win!")
