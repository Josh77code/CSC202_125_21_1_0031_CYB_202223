#Had or Tail Exercise
# import Random module
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")


# Banker roullite
import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# Split string
namesAsCSV = input("Give me everybody's names, separated by comma ")
names = namesAsCSV.split(",")
# Number of items 
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]
print(person_who_will_pay + "is going to buy the meal today")

# Rock scissors game


import random
import time

options = ['rock', 'paper', 'scissors']
score = {'player': 0, 'computer': 0}

while True:
    print('Ready!')
    time.sleep(1)
    print('Rock!')
    time.sleep(1)
    print('Paper!')
    time.sleep(1)
    print('Scissors!')
    time.sleep(1)

    player_choice = input('Choose rock, paper, or scissors: ')
    computer_choice = random.choice(options)

    print(f'You chose {player_choice}, computer chose {computer_choice}.')

    if player_choice == computer_choice:
        print('Tie!')
    elif (player_choice == 'rock' and computer_choice == 'scissors') or \
         (player_choice == 'paper' and computer_choice == 'rock') or \
         (player_choice == 'scissors' and computer_choice == 'paper'):
        print('You win!')
        score['player'] += 1
    else:
        print('Computer wins!')
        score['computer'] += 1

    print(f"Score - Player: {score['player']}, Computer: {score['computer']}\n")

    play_again = input('Do you want to play again? (y/n): ')

    if play_again.lower() != 'y':
        break



