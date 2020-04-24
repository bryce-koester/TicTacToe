import time

# set up keys for board
w, h = 3, 3
keys = [[0 for x in range(w)] for y in range(h)] 
keys[0][0] = '1'
keys[0][1] = '2'
keys[0][2] = '3'

keys[1][0] = '4'
keys[1][1] = '5'
keys[1][2] = '6'

keys[2][0] = '7'
keys[2][1] = '8'
keys[2][2] = '9'

# setup values for checkWinner and checkTie
i, j = 3, 3
values = [[0 for x in range(i)] for y in range(j)] 
for x in range(len(values)):
    for y in range(len(values[x])):
        values[x][y] = ' '

#method to make it look animated
def skip(lines):
    for i in range(lines):
        print('\n')

# method for printing board
def printBoard(values):
    print(values[0][0] + '|' + values[0][1] + '|' + values[0][2])
    print('-----')
    print(values[1][0] + '|' + values[1][1] + '|' + values[1][2])
    print('-----')
    print(values[2][0] + '|' + values[2][1] + '|' + values[2][2])
# method to check for a winner
def checkWinner(values):
    for x in range(len(values)):
        # check rows
        if((values[x][0] != ' ') & (values[x][0] == values[x][1]) & (values[x][1] == values[x][2])):
            return True
        # check columns
        if((values[0][x] != ' ') & (values[0][x] == values[1][x]) & (values[1][x] == values[2][x])):
            return True
    # check 1st diag
    if((values[1][1] != ' ') & (values[0][0] == values[1][1]) & (values[1][1] == values[2][2])):
        return True
    # check 2nd diag
    if((values[1][1] != ' ') & (values[0][2] == values[1][1]) & (values[1][1] == values[2][0])):
        return True
    else:
        return False

# method to check for tie
def checkTie(values):
    for x in range(len(values)):
        for y in range(len(values[x])):
            if (values[x][y] == ' '):
                return False
    return True
# method to check if either player can win on next turn
def winSpot(values):
    # bp1 = input('winspot called')
    w, h = 3, 3
    copy = [[0 for x in range(w)] for y in range(h)] 
    copy = copyBoard(values)
    # bp2 = input('copy created')
    i = 1
    for x in range(len(copy)):
        for y in range(len(copy[x])):
            # bp3 = input('iteration: ' + str(i))
            if (copy[x][y] == ' '):
                copy[x][y] = 'X'
                if (checkWinner(copy) == True):
                    return i
                else:
                    copy[x][y] = 'O'
                    if (checkWinner(copy) == True) :
                        return i
                    else:
                        copy[x][y] = ' '
                        i += 1
            else:
                i += 1
    return 0

# method to find best offensive move
# def offense(values):

# easy AI
def easyPlay(values):
    i = 1
    for x in range(len(values)):
        for y in range(len(values[x])):
            if (values[x][y] == ' '):
                return str(i)
            else:
                i += 1


# medium AI
def medPlay(values, isDumb):
    if (isDumb == True):
        return easyPlay(values)
    else:
        value = winSpot(values)
        if (value == 0):
            return easyPlay(values)
        else:
            return str(value)

# hard AI
def hardPlay(values):
    value = winSpot(values)
    if (value == 0):
        return easyPlay(values)
    else:
        return str(value)

# reset method to play again
def reset():
    for x in range(len(values)):
        for y in range(len(values[x])):
            values[x][y] = ' '
# method to copy the board
def copyBoard(values):
    i, j = 3, 3
    valuesCopy = [[0 for x in range(i)] for y in range(j)] 
    for x in range(len(values)):
        for y in range(len(values[x])):
            valuesCopy[x][y] = values[x][y]
    return valuesCopy
# method for taking a turn
def place(player, value):
    if ((int(value) < 0) | (int(value) > 9)):
            print('Invalid input')
            return False
    if (int(value) == 1):
        if(values[0][0] != ' '):
            print('Someone already played there, try again')
            return False
        else:
                values[0][0] = player
                return True
    if (int(value) == 2):
        if(values[0][1] != ' '):
            print('Someone already played there, try again')
            return False
        else:
                values[0][1] = player
                return True
    if (int(value) == 3):
        if(values[0][2] != ' '):
            print('Someone already played there, try again')
            return False
        else:
                values[0][2] = player
                return True
    if (int(value) == 4):
        if(values[1][0] != ' '):
            print('Someone already played there, try again')
            return False
        else:
                values[1][0] = player
                return True
    if (int(value) == 5):
        if(values[1][1] != ' '):
            print('Someone already played there, try again')
            return False
        else:
                values[1][1] = player
                return True
    if (int(value) == 6):
        if(values[1][2] != ' '):
            print('Someone already played there, try again')
            return False
        else:
                values[1][2] = player
                return True
    if (int(value) == 7):
        if(values[2][0] != ' '):
            print('Someone already played there, try again')
            return False
        else:
                values[2][0] = player
                return True
    if (int(value) == 8):
        if(values[2][1] != ' '):
            print('Someone already played there, try again')
            return False
        else:
                values[2][1] = player
                return True
    if (int(value) == 9):
        if(values[2][2] != ' '):
            print('Someone already played there, try again')
            return False
        else:
                values[2][2] = player
                return True
    else:
        return False

# start play, runs until player quits
def play(values, bot):
    printBoard(values)
    print('\n')
    xTurn = True
    turn = ''
    if(bot != 0):
        turn = input('Enter 1 to play first, 2 to go second\n')
        skip(1)
    if(str(turn) == '2'): 
        place('O', '5')
        print('AI is playing...')
        skip(1)
        # printBoard(values)
    player = 'X'
    isDumb = False
    while True:
        
        printBoard(values)
        skip(10)
        if (checkWinner(values)):
                # printBoard(values)
                skip(1)
                print('Player: ' + player + ' Wins!')
                value = input("Enter y to play again, c to change difficulty, or n to quit\n")
                if (value == 'n'):
                    break
                if(value == 'c'):
                    mode = input('Enter 1 for easy, 2 for medium, or 3 for hard\n')
                    print('Here is the starting board, lets play!')
                    print('\n')
                    reset()
                    play(values, int(mode))
                    break
                else:
                    reset()
        if (checkTie(values)):
            # printBoard(values)
            skip(1)
            print('Its a tie!')
            value = input("Enter y to play again, c to change difficulty, or n to quit\n")
            if (value == 'n'):
                break
            if(value == 'c'):
                mode = input('Enter 1 for easy, 2 for medium, or 3 for hard\n')
                print('Here is the starting board, lets play!')
                print('\n')
                reset()
                play(values, int(mode))
                break
            else:
                reset()
                play(values, bot)
                break
                print('\n')
                print('\n')
        # printBoard(values)
        if ((xTurn == False) & (bot == 1)):
            player = 'AI'
            value = easyPlay(values)
            place('O', value)
            xTurn = True
            print('AI is playing...')
            time.sleep(2)
            skip(10)
            # printBoard(values)
        elif ((xTurn == False) & (bot == 2)):
            player = 'AI'
            value = medPlay(values, isDumb)
            place('O', value)
            xTurn = True
            if(isDumb == True):
                isDumb = False
            else:
                isDumb = True
            print('AI is playing...')
            time.sleep(2)
            skip(10)
            # printBoard(values)
        elif ((xTurn == False) & (bot == 3)):
            player = 'AI'
            value = hardPlay(values)
            place('O', value)
            xTurn = True
            skip(1)
            print('AI is playing...')
            time.sleep(2)
            skip(10)
            # printBoard(values)
        else:
            if xTurn:
                player = 'X'
            else:
                player = 'O'
            print('\n')
            while(True):
                value = input("Player " + player + " Please type a number 1-9, or exit to quit:\n")
                if ('exit' in value.lower()):
                    print('game over')
                    break
                # print('you entered: ' + value)
                if(place(player, value) == True):
                    skip(3)
                    break
            if (xTurn): xTurn = False
            else: xTurn = True
           
# Intro
print('\n')
print('Welcome to Bryces TicTacToe!')
print('Each round enter a number corresponding to a spot on the board:\n')
printBoard(keys)
print('\n')
numPlayers = input("Enter 1 to play the AI, or 2 to play with a friend\n")
print('\n')
print('Select a difficulty: ')
if (numPlayers == '1'):
    mode = input('Enter 1 for easy, 2 for medium, or 3 for hard\n')
    if (mode == '1'):
        print('Here is the starting board, lets play!')
        print('\n')
        play(values, 1)
    if (mode == '2'):
        print('Here is the starting board, lets play!')
        print('\n')
        play(values, 2)
    if (mode == '3'):
        print('Here is the starting board, lets play!')
        print('\n')
        play(values, 3)
else:
    print('Here is the starting board, lets play!')
    print('\n')
    play(values, 0)
