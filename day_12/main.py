from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

secret_number = random.randint(1, 100)
#print(f"Pssst, the correct answer is {secret_number}")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5
else:
    print("Wrong difficulty level")
    attempts = 0

while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == secret_number:
        print(f"You got it! The answer was {secret_number}.")
        break
    elif guess > secret_number:
        print("Too high.\nGuess again.")
    else:
        print("Too low.\nGuess again.")
    attempts -= 1
