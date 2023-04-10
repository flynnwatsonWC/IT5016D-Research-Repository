import random

#This section is for you to guess the computer's number.
def guess(x):
    random_number = random.randint(1, x) #Creates a boundary on what number can be guessed up to, e.g 100
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ')) # a box where you write your answer
        if guess < random_number: 
            print('Sorry, guess again. Too low.') # possible outcome 
        elif guess > random_number:
            print('Sorry, guess again. Too high.') # possible outcome

    print(f'Yay, you have guessed the number {random_number} correctly!!') #Tells you you've guessed the correct number.

#This section is for the computer to guess your number.
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  # could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)?? ').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number, {guess}, correctly!') #Tells you the computer has guessed your number.


guess(100)
