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