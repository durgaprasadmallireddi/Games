import time
from os import system


def Graphics():
    intro = '____HANGMAN GAME____'
    print('\t',end='',flush=True)
    for i in intro:
        print(i,end='',flush=True)
        time.sleep(0.2)
    man = [' | ',' O ','/|\ ','/ \ ','','']
    print()
    print()
    print('\t',end='',flush=True)
    print('+',end='',flush=True)
    for i in range(7):
        print('-',end='',flush=True)
        time.sleep(0.1)
    print('+')
    for i in range(6):
        print('\t|',end='',flush=True)
        print(' '*5,man[i])
        time.sleep(0.2)
    print('\t',end='',flush=True)
    for i in range(11):
        print('=',end='',flush=True)
        time.sleep(0.1)
    print()
    print()
    print('\t',end='',flush=True)
    intro = 'Press Enter to Start the Game... :)'
    for i in intro:
        print(i,end='',flush=True)
        time.sleep(0.2)
        
    status = input()
    return

if __name__=='__main__':
    Graphics()