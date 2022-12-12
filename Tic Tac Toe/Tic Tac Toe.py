class Board:
    def __init__(self):
        self.board = [[1,2,3],[4,5,6],[7,8,9]]
    def printBoard(self):
        for i in range(3):
            for j in range(3):
                print(self.board[i][j],end ='')
                if j != 2:
                    print('|',end = '')
            print()
            if i == 2:
                break
            for k in range(3):
                print('-',end = '')
                if k != 2:
                    print('|',end = '')
            print()
    def makeMove(self,move,player_var):
        if move % 3 == 0:
            i = move//3
            j = 2
            self.board[i-1][j] = player_var
        else:
            i = move//3
            j = move % 3
            self.board[i][j-1] = player_var
        #print(player_var)
    def validMove(self,move):
        if move % 3 == 0:
            i = (move//3) - 1
            j = 2
        else:
            i = move//3
            j = (move % 3) - 1
        #print(i,j)
        if self.board[i][j] in ['x','o']:
            return False
        return True
    def win(self):
        flag = 0
        Winner = 'None'
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2]:
                Winner = self.board[i][0]
                flag = 1
                break
        if flag == 0:
            for i in range(3):
                if self.board[0][i] == self.board[1][i] == self.board[2][i]:
                    Winner = self.board[0][i]
                    flag = 1
                    break
        if flag == 0:
            # Checking Diagonals
            if self.board[0][0] == self.board[1][1] == self.board[2][2]:
                Winner = self.board[0][0]
                flag = 1
            elif self.board[0][2] == self.board[1][1] == self.board[2][0]:
                Winner = self.board[1][1]
                flag = 1
        
        return Winner
    def get_moves(self):
        moves = []
        for i in self.board:
            for j in i:
                if j not in ['x','o']:
                    moves.append(j)
        return moves
    def Comp_move(self,move,player_var):
        if move % 3 == 0:
            i = (move//3) - 1
            j = 2
        else:
            i = move//3
            j = (move % 3) - 1
        
        temp = self.board[i][j]
        self.board[i][j] = player_var
        if self.win() == 'None':
            self.board[i][j] = temp
            return 'None'
        else:
            self.board[i][j] = temp
            return True
    
        
class Player:
    def __init__(self,player_var):
        self.player_var = player_var

    def blockMove(self,Human_var,board):
        avail = board.get_moves()
        for i in avail:
            a = board.Comp_move(i,Human_var)
            if a == True:
                return i
        return -1
    def winningMove(self,board):
        avail = board.get_moves()
        for i in avail:
            a = board.Comp_move(int(i),self.player_var)
            if a == True:
                return i
        return -1
    def trickMove(self,board,player_var,comp_var):
        a = player_var
        b = comp_var
        #print(a)
        #Trickmove 1
        if board.board == [[a,2,3],[4,5,6],[7,8,9]]:
            #print(board)
            return 9
        #Trickmove 2
        if board.board == [[1,2,3],[4,a,6],[7,8,9]]:
            return 1
        #Trickmove 3
        if board.board == [[a,2,3],[4,a,6],[7,8,b]]:
            return 7
        else:
            return False
                

        
class Game:
    def start(self):
        print('choose option')
        print('\t 1.Player to player')
        print('\t 2.Play with computer')
        option = int(input('Enter:'))
        board = Board()
        if option == 1:
            var = input('Choose option for player 1 ("x"/"o"):')
            player1 = Player(var)
            var = input('Choose option for player 2 ("x"/"o"):')
            player2 = Player(var)
            board.printBoard()
            while board.win() == 'None':
                move = int(input('please enter 1-9 to make your move (0 to quit) Player 1:'))
                if move == 0:
                    break
                if board.validMove(move):
                    board.makeMove(move,player1.player_var)
                    board.printBoard()
                else:
                    print('Invalid Input! TRY AGAIN>>')
                    continue
                if board.win() != 'None':
                    print('Player 1',player1.player_var,'has won')
                    break
                avail = board.get_moves()
                #print(avail)
                if avail == []:
                    print('Its a TIE')
                    break
                move = int(input('please enter 1-9 to make your move (0 to quit) Player 1:'))
                if move == 0:
                    break
                if board.validMove(move):
                    board.makeMove(move,player2.player_var)
                    board.printBoard()
                else:
                    print('Invalid Input! TRY AGAIN>>')
                    continue
                if board.win() != 'None':
                    print('Player 2',player2.player_var,'has won')
                    break
                avail = board.get_moves()
                #print(avail)
                if avail == []:
                    print('Its a TIE')
                    break
                

        if option == 2:
            var = input('Choose option for player ("x"/"o"):')
            Human = Player(var)
            if var == 'x':
                Computer = Player('o')
            else:
                Computer = Player('x')
            #print(1111,board.win())
            while board.win() == 'None':
                board.printBoard()
                move = int(input('please enter 1-9 to make your move (0 to quit):'))
                if move == 0:
                    break
                if board.validMove(move):
                    board.makeMove(move,Human.player_var)
                    board.printBoard()
                else:
                    print('Invalid move! TRY AGAIN>>')
                    continue
                if board.win() != 'None':
                    print('Player',Human.player_var,'has won')
                    break
                print('Computers turn')
                a = Computer.trickMove(board,Human.player_var,Computer.player_var)
                #print(a)
                if a != False:
                    board.makeMove(a,Computer.player_var)
                    continue
                avail = board.get_moves()
                if avail == []:
                    print('Its a Tie')
                    break
                a = Computer.winningMove(board)
                #print('win',a)
                if a != -1:
                    #print('Winning move')
                    board.makeMove(a,Computer.player_var)
                    #print(board.win())
                    if board.win() != 'None':
                        board.printBoard()
                        print('Player',Computer.player_var,'has won')
                        break
                    else:
                        continue
                a = Computer.blockMove(Human.player_var,board)
                if a == -1:
                    board.makeMove(avail[0],Computer.player_var)
                    if board.win() != 'None':
                        print('Player',Computer.player_var,'has won')
                        break
                    continue
                else:
                    board.makeMove(a,Computer.player_var)
                    if board.win() != 'None':
                        print('Player',Computer.player_var,'has won')
                        break
        status = input('Enter to exit,please type (Y)es to continue:')
        if status == 'Y':
            Game().start()
            
            
                
        


        


# Main code
game = Game()
game.start()
