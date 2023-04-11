"""
Hangman implementation by Kylie Ying

YouTube Kylie Ying: https://www.youtube.com/ycubed 
Twitch KylieYing: https://www.twitch.tv/kylieying 
Twitter @kylieyying: https://twitter.com/kylieyying 
Instagram @kylieyying: https://www.instagram.com/kylieyying/ 
Website: https://www.kylieying.com
Github: https://www.github.com/kying18 
Programmer Beast Mode Spotify playlist: https://open.spotify.com/playlist/4Akns5EUb3gzmlXIdsJkPs?si=qGc4ubKRRYmPHAJAIrCxVQ 
"""

import random
from words import words #imports the word file from the word list into this file.
from hangman_visual import lives_visual_dict #imports the lives and visuals for the game.
import string


def get_valid_word(words):  #grabs words from words.py
    word = random.choice(words) #randomly chooses a word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words) 

    return word.upper()


def hangman(): #defines the main functions of the game.
    word = get_valid_word(words)
    word_letters = set(word)  # counts all of the letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user has guessed

    lives = 7

    # gets user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # ' '.join(['a', 'b', 'cd']) --> 'a b cd'
        print('You have', lives, 'lives left and you have used these letters: ', ' '.join(used_letters)) #prints how many lives you have left

        # what the current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print(lives_visual_dict[lives])
        print('Current word: ', ' '.join(word_list)) #shows the word with the letters you've correctly guessed.

        user_letter = input('Guess a letter: ').upper() #This asks you to guess a letter.
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter) #This adds letters that are not in the word, and adds them to a used letters list.
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print('')
              
            # takes away a life if wrong and tells you the letter you guessed is not in the word.
            else:
                lives = lives - 1  
                print('\nYour letter,', user_letter, 'is not in the word.')
                
           
        elif user_letter in used_letters:
            print('\nYou have already used that letter. Guess another letter.') # Reminds you a letter you guessed has already been used.
          
        else:
            print('\nThat is not a valid letter.') # This happens if you type a number or symbol.

    # gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0: #Indicates you have lost the game.
        print(lives_visual_dict[lives]) #The lives will print 0 if you've lost, or number of lives left if you won here.
        print('You died, sorry. The word was', word) # Prints the word you failed to guess.
    else:
        print('YAY! You guessed the word', word, '!!')# Prints the word you guessed correctly.


if __name__ == '__main__':
    hangman()
