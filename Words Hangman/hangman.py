from Graphic2 import Graphics as gp
from os import system
import random
#import time





def playagain():
    print('Wanna play again!!')
    response = input('press "y" or "yes" to play again,press "n" or "no" to STOP!! [y/n] : ').lower()
    if response == 'y' or response == 'yes' :
        hangman(getword())
    else:
        print('THANK YOU!!!')




def getword():
    words = open('words.txt','r').readlines()
    #print(words)
    word = random.choice(words)
    word = ''.join([letter for letter in word[1:] if letter.isalpha()])
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word
    
def hangman(word):
    #print(word)
    system('cls')
    temp = list(word)
    print('The word has',len(word),'letters')
    guess = ['-']*len(word)
    tried_letters = []
    guesses = 0
    lives = 10
    print('Lives left : ',lives)
    print('The Word : ',' '.join(guess))
    while word != ''.join(guess) and lives != 0:
        print()
        guess_letter = input('Guess a letter : ').lower()
        system('cls')
        if len(guess_letter)==1 and guess_letter.isalpha():
            guesses += 1
            if guess_letter in temp:
                ind = word.index(guess_letter)  
                #print('index',ind,temp,word)
                for i in range(len(word)):
                    if guess_letter == word[i]:
                        guess[i] = guess_letter
                temp.remove(guess_letter)
                tried_letters.append(guess_letter)
                print()
                print('The letter you guessed is in the the word :)')
            elif guess_letter in tried_letters:
                print()
                print('You already tried this letter, TRY AGAIN!!')
            else:
                tried_letters.append(guess_letter)
                lives -= 1
                print()
                print('Letter is not in the word, TRY AGAIN!!')
            print('Letters tried : ',*(sorted(tried_letters)))
            print('The word : ',' '.join(guess))
            print('No of Guesses : ',guesses)
            print('Lives left : ',lives)
        else:
            print('Enter the valid input...')
    print()
    if lives != 0:
        print('YAY!! YOU WON')
    else:
        print('YOU LOST!! The word is :',word.upper())
        print('You are out of lives.. TRY AGAIN!!')
    playagain()
            




#Starting the game with some graphics
system('cls')
gp()
hangman(getword())


