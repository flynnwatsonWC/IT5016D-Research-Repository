from random import shuffle


def shuffle_list(mylist):
    shuffle(mylist)
    return mylist


def player_guess():
    
    guess=''
    
    
    while guess not in ['0','1','2']:
        guess = input("Pick a number: 0, 1, or 2: ")
    return int(guess)


def check_guess(mylist,guess):
    if mylist[guess] == 'O':
        print("Correct!")
        
    else:
        print("Wrong guess!")
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
        
