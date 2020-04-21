# setup player board
w, h = 5, 5
board = [[0 for x in range(w)] for y in range(h)] 
board[0][0] = ' '
board[0][1] = '|'
board[0][2] = ' '
board[0][3] = '|'
board[0][4] = ' '

board[1][0] = '-'
board[1][1] = '-'
board[1][2] = '-'
board[1][3] = '-'
board[1][4] = '-'

board[2][0] = ' '
board[2][1] = '|'
board[2][2] = ' '
board[2][3] = '|'
board[2][4] = ' '

board[3][0] = '-'
board[3][1] = '-'
board[3][2] = '-'
board[3][3] = '-'
board[3][4] = '-'

board[4][0] = ' '
board[4][1] = '|'
board[4][2] = ' '
board[4][3] = '|'
board[4][4] = ' '

# set up keys for board
w, h = 5, 5
keys = [[0 for x in range(w)] for y in range(h)] 
keys[0][0] = '1'
keys[0][1] = '|'
keys[0][2] = '2'
keys[0][3] = '|'
keys[0][4] = '3'

keys[1][0] = '-'
keys[1][1] = '-'
keys[1][2] = '-'
keys[1][3] = '-'
keys[1][4] = '-'

keys[2][0] = '4'
keys[2][1] = '|'
keys[2][2] = '5'
keys[2][3] = '|'
keys[2][4] = '6'

keys[3][0] = '-'
keys[3][1] = '-'
keys[3][2] = '-'
keys[3][3] = '-'
keys[3][4] = '-'

keys[4][0] = '7'
keys[4][1] = '|'
keys[4][2] = '8'
keys[4][3] = '|'
keys[4][4] = '9'

# setup values for checkWinner and checkTie
i, j = 3, 3
values = [[0 for x in range(i)] for y in range(j)] 
for x in range(len(values)):
    for y in range(len(values[x])):
        values[x][y] = ''

# method for printing board
def printBoard(board):
    for x in range(len(board)):
        row = ''
        for y in range(len(board[x])):
            row += board[x][y]
        print(row)

# method to check for a winner
def checkWinner(values):
    for x in range(len(values)):
        # check rows
        if((values[x][0] != '') & (values[x][0] == values[x][1]) & (values[x][1] == values[x][2])):
            return True
        # check columns
        if((values[0][x] != '') & (values[0][x] == values[1][x]) & (values[1][x] == values[2][x])):
            return True
    # check 1st diag
    if((values[1][1] != '') & (values[0][0] == values[1][1]) & (values[1][1] == values [2][2])):
        return True
    # check 2nd diag
    if((values[1][1] != '') & (values[0][2] == values[1][1]) & (values[1][1] == values [2][0])):
        return True
    else:
        return False

# method to check for tie
def checkTie(values):
    for x in range(len(values)):
        for y in range(len(values[x])):
            if (values[x][y] == ''):
                return False
    return True

# store copy of blank board for reset
w, h = 5, 5
boardCopy = [[0 for x in range(w)] for y in range(h)]  
for x in range(len(boardCopy)):
    for y in range(len(boardCopy[x])):
        boardCopy[x][y] = board[x][y]

# store copy of blank values for reset
w, h = 3, 3
valuesCopy = [[0 for x in range(w)] for y in range(h)]
for x in range(len(valuesCopy)):
    for y in range(len(valuesCopy[x])):
        valuesCopy[x][y] = values[x][y]
player = ''
xTurn = True

# Intro
print('\n')
print('Welcome to Bryces TicTacToe!')
print('Each round enter a number corresponding to a spot on the board:\n')
printBoard(keys)
print('\n')
print('Here is the starting board, lets play!')
print('\n')

# start play, runs until player quits
while True:
    printBoard(board)
    if xTurn:
        player = 'X'
    else:
        player = 'O'
    print('\n')
    value = input("Player " + player + " Please type a number 1-9, or exit to quit:\n")
    if ('exit' in value.lower()):
        print('game over')
        break
    print('you entered: ' + value)
    if ((int(value) < 0) | (int(value) > 9)):
        print('Invalid input')
    if (int(value) == 1):
        if(values[0][0] != ''):
            print('Someone already played there, try again')
        else:
            if(xTurn):
                board[0][0] = 'X'
                values[0][0] = 'X'
                xTurn = False
            else:
                board[0][0] = 'O'
                values[0][0] = 'O'
                xTurn = True 
    if (int(value) == 2):
        if(values[0][1] != ''):
            print('Someone already played there, try again')
        else:
            if(xTurn):
                board[0][2] = 'X'
                values[0][1] = 'X'
                xTurn = False
            else:
                board[0][2] = 'O'
                values[0][1] = 'O'
                xTurn = True 
    if (int(value) == 3):
        if(values[0][2] != ''):
            print('Someone already played there, try again')
        else:
            if(xTurn):
                board[0][4] = 'X'
                values[0][2] = 'X'
                xTurn = False
            else:
                board[0][4] = 'O'
                values[0][2] = 'O'
                xTurn = True 
    if (int(value) == 4):
        if(values[1][0] != ''):
            print('Someone already played there, try again')
        else:
            if(xTurn):
                board[2][0] = 'X'
                values[1][0] = 'X'
                xTurn = False
            else:
                board[2][0] = 'O'
                values[1][0] = 'O'
                xTurn = True 
    if (int(value) == 5):
        if(values[1][1] != ''):
            print('Someone already played there, try again')
        else:
            if(xTurn):
                board[2][2] = 'X'
                values[1][1] = 'X'
                xTurn = False
            else:
                board[2][2] = 'O'
                values[1][1] = 'O'
                xTurn = True 
    if (int(value) == 6):
        if(values[1][2] != ''):
            print('Someone already played there, try again')
        else:
            if(xTurn):
                board[2][4] = 'X'
                values[1][2] = 'X'
                xTurn = False
            else:
                board[2][4] = 'O'
                values[1][2] = 'O'
                xTurn = True 
    if (int(value) == 7):
        if(values[2][0] != ''):
            print('Someone already played there, try again')
        else:
            if(xTurn):
                board[4][0] = 'X'
                values[2][0] = 'X'
                xTurn = False
            else:
                board[4][0] = 'O'
                values[2][0] = 'O'
                xTurn = True 
    if (int(value) == 8):
        if(values[2][1] != ''):
            print('Someone already played there, try again')
        else:
            if(xTurn):
                board[4][2] = 'X'
                values[2][1] = 'X'
                xTurn = False
            else:
                board[4][2] = 'O'
                values[2][1] = 'O'
                xTurn = True 
    if (int(value) == 9):
        if(values[2][2] != ''):
            print('Someone already played there, try again')
        else:
            if(xTurn):
                board[4][4] = 'X'
                values[2][2] = 'X'
                xTurn = False
            else:
                board[4][4] = 'O'
                values[2][2] = 'O'
                xTurn = True 
    if (checkWinner(values)):
        printBoard(board)
        print('Player: ' + player + ' Wins!')
        value = input("Enter y to play again, or n to quit\n")
        if (value == 'n'):
            break
        else:
            board = boardCopy
            values = valuesCopy
    else:
        if (checkTie(values)):
            printBoard(board)
            print('Its a tie!')
            value = input("Enter y to play again, or n to quit\n")
            if (value == 'n'):
                break
            else:
                board = boardCopy
                values = valuesCopy
                print('\n')
                print('\n')
