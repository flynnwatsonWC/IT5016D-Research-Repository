from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess(): #Defines guess.
    
    guess=''
    
    
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1, or 2: ") #This input asks you again if you do not put in a zero, one, or a two.
    return int(guess)


def check_guess(mylist,guess):
    if mylist[guess] == 'O': #This if statement shows that you guessed the correct answer.
        print("Correct!")
        
    else:
        print("Wrong guess!") #This else statement will run if your guess was wrong and prints the list to show you where the 'ball' was.
        print(mylist)

retry = True
while retry: #If the player wants to play again, this part will run as well as the part that resets the game at the bottom.
    
    mylist = [' ', 'O',' '] #This is the initial list

    mixedup_list = shuffle_list(mylist)  #This shuffles the list

    guess = player_guess() #This is for the players guess.

    check_guess(mixedup_list,guess) #This checks the guess.
    
   #This resets the game
    answer = input("Press Y to play again\n").lower()
    if answer == 'y':
        continue
    else: 
        retry = False
        continue
        
