# import the time module
# import time

# define the countdown func.
# def countdown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = '{:02d}:{:02d}'.format(mins, secs)
#         print(timer, end="\r")
#         time.sleep(1)
#         t -= 1
#
#
#






def display_board(board):
    print('+-------------+')
    print('|    |   |    |')
    print('|  ' + board[7] + ' | '+ board[8]+' | ' +board[9]+'  |')
    print('|    |   |    |')
    print('+-------------+')
    print('|    |   |    |')
    print('|  '+ board[4] + ' | '+ board[5]+' | ' +board[6]+'  |')
    print('|    |   |    |')
    print('+-------------+')
    print('|    |   |    |')
    print('|  '+ board[1] + ' | '+ board[2]+' | ' +board[3]+'  |')
    print('|    |   |    |')
    print('+-------------+')

# board = [' ','X','X','X','O','O','O','X','X','X']
# display_board(board)



#  Accepting Player input
def player_input():
    marker = ''
    while not (marker == 'O' or marker =='X'):
        marker = input("Player 1: Do you want to be 'X' or 'O' ?").upper()
    if(marker == 'O'):
        return ('O','X')
    else:
        return ('X','O')
# player_input()

# Function to place the marker
def place_marker(board,marker,position):
    board[position] = marker

# Function to check if player has won or lost
def win_check(board,mark):
    return(
        (board[7]==mark and board[8]==mark and board[9]==mark) or
        (board[4]==mark and board[5]==mark and board[6]==mark) or
        (board[1]==mark and board[2]==mark and board[3]==mark) or
        (board[7]==mark and board[4]==mark and board[1]==mark) or
        (board[8]==mark and board[5]==mark and board[2]==mark) or
        (board[9]==mark and board[6]==mark and board[3]==mark) or
        (board[7]==mark and board[5]==mark and board[3]==mark) or
        (board[9]==mark and board[5]==mark and board[1]==mark))


# Function to randomly choose which player goes first
import random
def choose_first():
    if random.randint(0,1) == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# Function to check if position on board is avalable
def space_check(board,position):
    return board[position] == ' '


# Function to check if board is full
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

# Function to check payer's choice
def player_choice(board):

    position = ' '
    while position not in '1 2 3 4 5 6 7 8 9'.split() or not space_check(board, int(position)):
        position = input('Choose your next position (1-9)')
    return int(position)

# Function to determine whether the user wants to play again
def replay():
    return input('Do you wan to play again. Yes or No').lower().startswith('y')


# Function to put all together
print('Welcome to TicTacToe')

while True:
    theBoard = [' ']*10
    player1_marker,player2_marker = player_input()
    turn = choose_first()
    print(turn + 'will go first')


    game_on = True


    while game_on:
        if turn == 'Player 1':

            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player1_marker,position)

            if win_check(theBoard,player1_marker):
                display_board(theBoard)
                print("Congratulations, Player 1 has won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is draw')
                    break
                else:
                    turn = 'Player 2'
        #     AI's turn
        else:
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard,player2_marker,position)

            if win_check(theBoard,player2_marker):
                display_board(theBoard)
                print("Congratulations, Player 2 has won the game!")
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print('The game is draw')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break