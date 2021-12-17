from colorama import init

def main():
    #print
    init()
    green = '\u001b[38;5;28m'
    reset = '\u001b[0m'
    lightBlue = '\u001b[38;5;39m'
    print(green + 'Mom can we have connect4 at home? \nConnect4 at home: \nCopyright Sean Software 2021\n' + reset)
    print('Player1 will play as O\nPlayer2 will play as X\n')

    #ask for player's name 
    player1Name = input('Player 1 name: ')
    player2Name = input('Player 2 name: ')
    player1 = player(player1Name, '\u001b[31mO\u001b[0m')
    player2 = player(player2Name, '\u001b[34mX\u001b[0m')
    print('\n')
    #create a board 7x6+1 for indexing
    board = [['1', '2', '3', '4', '5', '6', '7\n']]
    
    #populate
    winner = None
    for i in range(6):
        boardLine = ['-', '-', '-', '-', '-', '-', '-']
        board.append(boardLine)
    printBoard(board)
    #start turns 
    turn = 1
    while not isBoardFull(board) and not winner:
        if turn == 1:
            currentPlayer = player1
            turn = 0
        else:
            currentPlayer = player2
            turn = 1
        try:
            print('\n')
            drop = int(input(f'{currentPlayer.name}, which column you want to drop: \n')) - 1
            print('\n')
        except:
            print('Must be an integer')
            #function to update the board DONE
        if drop > 6 or drop < 0 :
            print("ERROR")
        else:
            currentBoard = dropToBoard(board, currentPlayer.item, drop)
            printBoard(currentBoard)
            winner = getWinner(currentBoard, currentPlayer)
    if winner:
        print(f'{lightBlue}Congratulations! {winner} has won the game!!{reset}\n')
    #print(isBoardFull(board))
    
    
def printBoard(board: list):
    for i in range(len(board)):
        output = ''
        for j in range(len(board[i])):
            output += board[i][j] + '\t'
        print(output + '\n')

def isBoardFull(board: list):
    defaultCell = 0
    for i in range(1, len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '-':
                defaultCell += 1
    
    if defaultCell == 0 :
        return True
    return False

def dropToBoard(board, item, column: int) :
    #move the item down the board unless theres item below or on edge
    for i in range(1, len(board)):
        if i < len(board) - 1 :
            if board[i + 1][column] != '-' and board[i][column] == '-':
                
                board[i][column] = item
                return board
        elif board[i][column] == '-':
            board[i][column] = item
            return board
        else:
            print('\ninvalid move\n')
            return board
            
            
    return None
            
#check to check if there is a winner
def getWinner(board, player):
    iMax = len(board) - 1
    #horizontal
    for i in range(len(board)):
        consec = 0
        for j in range(len(board[i])):
            if board[i][j] == player.item:
                consec += 1
                if consec == 4:
                    return player.name
            else:
                consec = 0
    #vertical
    for i in range(len(board[1])):
        consec = 0
        for d in range(len(board)):
            if board[d][i] == player.item:
                consec += 1
                if consec == 4:
                    return player.name
            else:
                consec = 0
    rows = len(board)
    columns = len(board[0])
    for i in range(rows):
        for j in range(columns):
            if board[i][j] == player.item:
                consec = 0
                col = j
                row = i
                #down right
                while col < columns and row < rows:
                    
                    if board[row][col] == player.item:
                        consec += 1
                        
                        
                        if consec == 4:
                            return player.name
                    col += 1
                    row += 1
                #reset the params
                col = j
                row = i
                consec = 0
                #down left
                while col > 0 and row < rows:
                    
                    if board[row][col] == player.item:
                        consec += 1
                        
                        
                        if consec == 4:
                            return player.name
                    col -= 1
                    row += 1
    return None
    #diagonal
    

class player:
    def __init__(self, name, item):
        self.name = name
        self.item = item


if __name__ == '__main__':
    main()