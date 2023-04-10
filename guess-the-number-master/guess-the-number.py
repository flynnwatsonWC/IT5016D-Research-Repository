#This section is for you to guess the computer's number.

import random

def guess(x):
    random_number = random.randint(1, x) #Creates a boundary on what number can be guessed up to, e.g 100
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) #Write your answer here.
        if guess < random_number: 
            print('Sorry, guess again. Too low.') #Tells you the number you guessed is too low.
        elif guess > random_number:
            print('Sorry, guess again. Too high.') #Tells you the number you guessed is too high.

    print(f'Yay, you have guessed the number {random_number} correctly!!') #Tells you you've guessed the correct number.

guess(100)
    

    
#This section is for the computer to guess your number.

import random

def computer_guess(x):
    low = 1 #Sets the lowest number the computer can guess.
    high = x #Sets the highest number the computer can guess.
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high) #
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower() #The computer asking you if your guess is too high, too low, or correct.
        if feedback == 'h':
            high = guess - 1 #The computer will understand that the guess is too high, and will guess a different number that is lower.
        elif feedback == 'l':
            low = guess + 1  #The computer will understand that the guess is too low, and will guess a different number that is higher.

    print(f'Yay! The computer guessed your number, {guess}, correctly!') #Tells you the computer has guessed your number.


computer_guess(100)
