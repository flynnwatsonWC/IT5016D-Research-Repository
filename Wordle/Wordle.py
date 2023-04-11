# Wordle (In the Terminal)
# By @TokyoEdtech
# Python 3.x
# Topics: input, slices, loops, ANSI color codes

import os, random
os.system("clear") #clears the screen ("clear" works for Mac and Linux)

#Colour Codes
BG_GREEN = "\u001b[42m" #letters in green indicates the word is the right letter in the right place.
BG_YELLOW = "\u001b[43m" #letters in yellow indicates the word is a right letter, but it's in the wrong place.
RESET = "\u001b[0m" #letters that aren't colour coded are letters that are not in the word.

#Game Title
print("WORDLE")

#Preparing and starting the game
correct = random.choice(["SHAKE", "SHARE", "PANIC", "AMUSE", "SHADE", "ABYSS", "YACHT", "ZIPPY", "ABACK", "TODAY", "BEAST", "ZESTY", "ALIVE", "ANGRY", "QUACK", "SCENT", "SAFER", "SHORT", "TENSE", "RINSE", "BORED", "TIGHT", "RIGHT," "NIGHT", "FIGHT", "MOURN", "HEAVY", "JUICY", "LAUGH", "LEGAL", "LEVEL", "LIGHT", "LOOKS", "CHEAP", "DAILY", "DIRTY", "PILCH" "EARLY", "HANDY",]) #A list of words that will be randomly chosen for the game.
for _ in range(6): # You get six chances to guess
    guess = input("Please guess. > ").upper() #Asks you to guess a word. (.upper() changes the word to uppercase automatically.)

    # Checks each letter
    for i in range(0, 5):
        if guess[i]==correct[i]:
            print(f"{BG_GREEN}{guess[i]}{RESET}", end="") #This tells you that one or more letters are correct, and in the correct place.
        elif guess[i] in correct:
            print(f"{BG_YELLOW}{guess[i]}{RESET}", end="")#This tells you that one or more letters are correct, but in the wrong place. 
        else:
            print(guess[i], end="") #end="" makes the word to stay on one line.
            
    print()

    # If you guessed the word.
    if guess == correct:
        print("You win!")
        exit()
 #If you didn't guess the word.
print("You lose!")
print(f"The correct word was {correct}.")
