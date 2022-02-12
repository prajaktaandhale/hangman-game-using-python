import random 
import string 
from words import words 
from hangman_drawing import user_lives 

def get_valid_word(words):
    word = random.choice(words)

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()

def hangman():

    lives = 6

    word = get_valid_word(words)

    word_letters = set(word) #letters of the word chosen
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    #taking input
    while len(word_letters) > 0 and lives > 0:
        print("you have "+ str(lives) + "lives" + "you've guessed these letters " +' ' .join(used_letters))
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("current word: " + ','.join(word_list))

        user_input = input("guess a letter: ").upper()

    #checking user input validity
        if user_input in alphabet - used_letters:
            used_letters.add(user_input)

            if user_input in word_letters: #guessing the correct letter
                word_letters.remove(user_input)
            
            else: #guessing the wrong letter
                lives = lives - 1              
                print("letter is not in the word, try again")
                print(" you have " + str(lives) + "lives remaining")
                user_lives(lives)
     
        elif user_input in used_letters:
            print("you've already guessed this letter, try again")
        
        else:
            print("invalid character, try again")

        
    if lives == 0:
        print("too bad, better luck next time! The word was: "+ word)
    
    else:
        print("you've guess the word " + word)
        print("you're winner!!!!")

hangman()

           




