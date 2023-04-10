# Wordle (In the Terminal)
# By @TokyoEdtech
# Python 3.x
# Topics: input, slices, loops, ANSI color codes

import os, random
os.system("clear")

BG_GREEN = "\u001b[42m" #letters in green indicates the word is the right letter in the right place.
BG_YELLOW = "\u001b[43m" #letters in yellow indicates the word is a right letter, but it's in the wrong place.
RESET = "\u001b[0m"

print("WORDLE")

correct = random.choice(["SHAKE", "SHARE", "PANIC", "AMUSE", "SHADE", "ABYSS", "YACHT", "TODAY", "BEAST", "MOURN", "PILCH"]) #words that will be randomly chosen for the game
for _ in range(6): # You get six chances to guess
    guess = input("Please guess. > ").upper() #.upper() changes the word to uppercase automatically.

    # Checks each letter
    for i in range(0, 5):
        if guess[i]==correct[i]:
            print(f"{BG_GREEN}{guess[i]}{RESET}", end="")
        elif guess[i] in correct:
            print(f"{BG_YELLOW}{guess[i]}{RESET}", end="")
        else:
            print(guess[i], end="")
            
    print()

    # If the guess is correct
    if guess == correct:
        print("You win!")
        exit()
 #If the guess is incorrect
print("You lose!")
print(f"The correct word was {correct}.")
