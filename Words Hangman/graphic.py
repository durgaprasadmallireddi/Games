from os import system
import time
def Graphics():
    graphics = ['''
      +-------+
      |       |
      |
      |
      |
      |
      |
      =========
      =========
      ''',
      '''
      +-------+
      |       |
      |       O
      |
      |
      |
      |
      =========
      =========
      ''',
      '''
      +-------+
      |       |
      |       O
      |       |
      |
      |
      |
      =========
      =========
      ''',
      '''
      +-------+
      |       |
      |       O
      |      /|\ 
      |
      |
      |
      =========
      =========
      ''',
      '''
      +-------+
      |       |
      |       O
      |      /|\ 
      |      / \ 
      |
      |
      =========
      =========
      ''']
    for graphic in graphics[:-1]:
        print(graphic,flush=True)
        print()
        print()
        #print('Press enter to start the game...')
        time.sleep(0.7)
        system('cls')
    print(graphics[-1])
    print()
    print()
    print('Press Enter to Start the Game...')


if __name__ == '__main__':
    Graphics()

    