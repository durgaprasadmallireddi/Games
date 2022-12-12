# This is a Rock Paper Scissors Game in python
# It is done using random module in python




import random
from os import system
import time


# This is a function to check if the given input is Valid
def checkValid(var,lis):
    while True:
        if var not in lis:
            var = input(f'Please enter Valid input({lis}) : ')
        else:
            break
    return var



# This is a function to print the rules to the user
def rules():
    system('cls')
    print('''   These are the rules of the game...
          
          its just a game of choices, The computer makes a choice and you make a choice,
          it is just the superiority of a choice over the other....
          
         your choice must be one of these three choices [ROCK,PAPER,SCISSORS]...
         The priority stands as below....
         ROCK beats the SCISSORS
         PAPER beats the ROCK
         SCISSORS beat the PAPER
         
         It is a cycle Thats why the game was interesting...
         if your choice is ROCK and Computers is SCISSORS you WIN and VICEVERSA
         ''')



def Game(turn1,turn2):
    #returns True when user Wins the game
    if (turn1 == 'r' and turn2 == 's') or (turn1 == 'p' and turn2 == 'r') or (turn1 == 's' and turn2 == 'p'):
        return True
    return False
        
            




#MAIN CODE
print('''      This is a Rock Paper And Scissors Game...
      There's no need of introduction to this game... it's quite popular right!!!
      But for those Who dont know the rules simply type enter '1' in the input below to display the rules...
      Else press 'Enter' to start the game...
          ''')    
intial = input('Enter your input here : ')
intail = checkValid(intial,['','1'])
if intial == '1':
    rules()
elif intial == '':
        while True:
            system('cls')
            list_of_elements = ['r','p','s']
            computer_turn = random.choice(list_of_elements)
            #print(computer_turn)
            print('              Computer has its choice(Hidden)')
            print()
            print('''              Now Please pick your choice...
                Enter 'r' for ROCK...
                Enter 'p' for PAPER...
                Enter 's' for SCISSORS... 
                ''')
            user_turn = input('Enter your Choice : ')
            print('Ready',end='-->')
            time.sleep(1)
            for i in range(5,1,-1):
                print(i,end='-->',flush=True)
                time.sleep(1)
            print(1)
            system('cls')
            
            print('Your choice is ',user_turn,' Computers choice is ',computer_turn)
            if user_turn == computer_turn:
                print("It's a DRAW!!")
            elif Game(user_turn,computer_turn):
                print('YOU WON!!')
            else:
                print('YOU LOST!!')
            print('Wanna Play again!!')
            Again = input('press "y" to play again, "n" to stop : ')
            Again = checkValid(Again,['y','n'])
            if Again == 'n':
                break