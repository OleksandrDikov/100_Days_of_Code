import random

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)
guess = input("Input a latter: ").lower()

for l in chosen_word:
  if guess == l:
    print("Correct")
  else:
    print("Wrong")
