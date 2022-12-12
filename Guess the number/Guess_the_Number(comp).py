# This is a Game in which Computer has a secret number and you have to Guess it...!!!
# You Guess the number And computer says if the number you guessed is higher or Lower than the Secret Number And you guess again
# if you guess the actual number you win
# Computer counts the number of tries you have taken to  guess the number and Prints it....
# Let's Get Started

from random import randint
from os import system

def checkValid(var,lis):
    while True:
        if var not in lis:
            var = input(f'Please enter Valid input({lis}) : ')
        else:
            break
    return var
    
# Here is the Code for easy level
def Easy_level():
    system('cls')
    print('Provide the Range in which you wanna guess the number.')
    upper_bound = int(input('Enter the Upper_Bound: '))
    lower_bound = int(input('Enter the Lower_Bound: '))

    # Here's The Secret Number
    Secret_Number = randint(upper_bound,lower_bound)
    # Now the secret number is Ready


    # It's Time for player Guessing the number
    print('The Secret Number is Ready...')
    No_of_Tries = 0

    # Here's the logic for the game
    while True:
        Guess = int(input(('Guess the Number : ')))
        No_of_Tries += 1
        if Guess == Secret_Number:
            print('You won...')
            print("No of Tries you've taken for Guessing Number is ",No_of_Tries )
            break
        elif Guess > Secret_Number:
            if Guess-Secret_Number > 10:
                print('Nope!! WRONG GUESS...THE NUMBER YOU GUESSED IS TOO HIGH... TRY AGAIN...')
            else:
                print('Nope!! WRONG GUESS...THE NUMBER YOU GUESSED IS HIGH... BUT YOU ARE CLOSE!!! TRY AGAIN...')
        else:
            if Secret_Number-Guess > 10:
                print('Nope!! WRONG GUESS...THE NUMBER YOU GUESSED IS TOO LOW... TRY AGAIN...')
            else:
                print('Nope!! WRONG GUESS...THE NUMBER YOU GUESSED IS LOW... BUT YOU ARE CLOSE!!! TRY AGAIN...')

# Here's The code for medium level
def Medium_and_Hard_level(n,r):
    system('cls')
    No_of_guesses = n
    Secret_Number = randint(0,r)
    while No_of_guesses != 0:
        print('Guesses Left = {}'.format(No_of_guesses))
        Guess = int(input('Guess The Number : '))
        No_of_guesses -= 1
        if Guess == Secret_Number:
            print('YOU WON...')
        elif Guess > Secret_Number:
            print('NOPE.... WRONG GUESS... YOU HAD IT TOO HIGH... TRY AGAIN')
        else:
            print('NOPE.... WRONG GUESS... YOU HAD IT TOO LOW... TRY AGAIN')
    if No_of_guesses == 0:
        print()
        print()
        print('OHH!.. SEEMS LIKE YOU RAN OUT OF GUESSES... YOU LOST!!')




#MAIN CODE
system('cls')
print('About The Game....')
print('''
      This is a Game in which Computer has a secret number and you have to Guess it...!!!
      You Guess the number And computer says if the number you guessed is higher or Lower than
      the Secret Number And you guess again
      if you guess the actual number you win
      Computer counts the number of tries you have taken to  guess the number and Prints it....
      Let's Get Started
        ''')
print()
print()
start = input('Press Enter to start the Game...')


while True:
    system('cls')
    # lets add some levels to the Game
    print('''Please Select the level You Wanna Play...
                For Easy --> Press 1
                For Medium --> Press 2
                For Hard --> Press 3
            In Easy level You have Unlimited Tries for guessing the number and if your guess close 
            to the Secret Number(i.e difference is less than 10) then you will get a hint that 'YOU ARE TOO CLOSE'
            and you can choose the range of number you are guessing
            
            In Medium Level You have 10 guesses to guess the number if you guess the number in 10 guesses you Win
            There Are no extra hints in this level and you cant choose the range. Here the range is 0 to 100.
            
            In Hard Level You Have 5 Guesses to guess the number and Here the range is 0 to 500''')
    print()
    print()
    level = int(input('Please Choose The Level : '))
    level = checkValid(level,[1,2,3])
    
    
    # Entering into the Game Based on Selected level
    
    if level == 1:
        Easy_level()
    elif level == 2:
        Medium_and_Hard_level(10,100)
    else:
        Medium_and_Hard_level(5,500)
    
    print('''  
             Wanna Play again...
             If yes --> press 'y' 
             If No --> press 'n' ''')
    play_again = input()
    play_again = checkValid(play_again,['y','n'])
    if play_again == 'n':
        break
        