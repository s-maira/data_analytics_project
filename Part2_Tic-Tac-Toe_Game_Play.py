#  A simple Tic-Tac-Toe game
# Players 'X' and 'O' take turn inputing their position on the command line using numbers 1-9
# 1 | 2 | 3
# ---------
# 4 | 5 | 6
# ---------
# 7 | 8 | 9
#


# The Game Board 
from tkinter.tix import INTEGER

board = {
    1: '1', 2: '2', 3: '3',
    4: '4', 5: '5', 6: '6',
    7: '7', 8: '8', 9: '9'
    }


# TODO: update the gameboard with the user input
def markBoard(position, mark):
    board[position] = mark


# TODO: print the game board as described at the top of this code skeleton
# Will not be tested in Part 1
def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('-----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('-----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


# TODO: check for wrong input, this function should return True or False.
# True denoting that the user input is correct
# you will need to check for wrong input (user is entering invalid position) or position is out of bound
# another case is that the position is already occupied
def validateMove(position):
    position = str(position)
    if not str(position).isdigit():
        return False

    position = int(position)
    if position < 1 or position > 9:
        return False

    if board[position] == 'X' or board[position] == 'O':
        return False
        
    else:
        return True


# TODO: list out all the combinations of winning, you will neeed this
# one of the winning combinations is already done for you
winCombinations = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 4, 7],
    [2, 5, 8],
    [3, 6, 9],
    [1, 5, 9],
    [3, 5, 7]
]


# TODO: implement a logic to check if the previous winner just win
# This method should return with True or False
def checkWin(player):
    return any(all(board[position] == player for position in line) for line in winCombinations)


# TODO: implement a function to check if the game board is already full
# For tic-tac-toe, tie bascially means the whole board is already occupied
# This function should return with boolean
def checkFull():
    for position in range(1,10):
        if validateMove(position):
            return False
    return True


#########################################################
## Copy all your code/fucntions in Part 1 to above lines
## (Without Test Cases)
#########################################################


# entry point of the whole program
print("\n")
print("*****Welcome to Tic Tac Toe Game!*****")
print('Game started: \n\n' +
    ' 1 | 2 | 3 \n' +
    ' --------- \n' +
    ' 4 | 5 | 6 \n' +
    ' --------- \n' +
    ' 7 | 8 | 9 \n')

# TODO: Complete the game play logic below
# You could reference the following flow
# 1. Ask for user input and validate the input
# 2. Update the board
# 3. Check win or tie situation
# 4. Switch User

def gamePlay():

    gameEnded = False
    currentTurnPlayer = 'X'

    while not gameEnded:
    #this loop is start the gameplay()

        position = input(currentTurnPlayer + " please enter your position: ")
        #to ask the player for their input or desired position

        if str(position).isdigit() :
            position = int(position)


        if validateMove(position):
            markBoard(position, currentTurnPlayer)
            printBoard(board)
        #if the position is validated, then the mark will be updated on the game board
        
        else:
            print("position invalid or occupied")
            printBoard(board)
            continue
        #if the position is invalid, user will continue to be asked for their position

        if checkWin(currentTurnPlayer):
            gameEnded = True
            print ("Result: " + currentTurnPlayer +" has won the game!")
            break
        #to break the gameplay() loop once there is a winner

        if checkFull():
            gameEnded = True
            print("Result: it's a tie!")
            break
        #to break the gameplay() loop when all board grid is filled/game is tie
            
        if currentTurnPlayer == "X":
            currentTurnPlayer = "O"
        else:
            currentTurnPlayer = "X" 
        #to switch the player while the game is on   

gamePlay()
#to play the game


# Bonus Point: Implement the feature for the user to restart the game after a tie or game over

gameRestart = True

while gameRestart:
#this loop is to restart the game 

    restart = input("Would you like to play another game? (Y/N): ")
    #to ask the player if they want to play for another round
        
    if restart.upper() == "Y":

        board = {
            1: '1', 2: '2', 3: '3',
            4: '4', 5: '5', 6: '6',
            7: '7', 8: '8', 9: '9'
            }
        #to restart a new board
            
        print('Game started: \n\n' +
            ' 1 | 2 | 3 \n' +
            ' --------- \n' +
            ' 4 | 5 | 6 \n' +
            ' --------- \n' +
            ' 7 | 8 | 9 \n')
        #to re-enter the entry point of the program

        gamePlay()
        continue
        #to continue the gamePlay() loop until the user chooses otherwise

    elif restart.upper() == "N":
        print("OK then, see you later!")
        break
        #break the gameRestart loop and exit the program















        
        


