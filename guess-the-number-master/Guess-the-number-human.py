#This section is for you to guess the computer's number.

import random

def guess(x):
    random_number = random.randint(1, x) #Creates a boundary on what number can be guessed up to, e.g 100
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) #Write your answer here.
        if guess < random_number: 
            print('Sorry, guess again. \n Too low.') #Tells you the number you guessed is too low.
        elif guess > random_number:
            print('Sorry, guess again. \n Too high.') #Tells you the number you guessed is too high.

    print(f'Yay, you have guessed the number {random_number} correctly!!') #Tells you you've guessed the correct number.

guess(100)
