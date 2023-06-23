# Python list
import random
word_list = ["Josh", "sam","Mike"]
choosen_word = random.choice(word_list)
print(f'passt, the solution is {chosen_word}.')
display = []
for_in range(len(choosen_word)):
display += "_"
print(display)
guess = input("Guess a letter: ").lower

for position in range(len(choosen_word)):
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

