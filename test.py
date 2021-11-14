

test_board = ['X','O','X','O','X','O','X','O','X']


def win_check(board, mark):
    pass
def display_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[6]} | {board[7]} | {board[8]}')


def player_input():
    player1 = input("Please pick a marker 'X' or 'O'")
    if player1 == 'o':
        player2 = 'x'
    else:
        player2 = 'o'

    while(win_check):
        position = int(input('Please enter a number'))
        test_board[position-1] = player1
        position2 = int(input('Please enter a number'))
        test_board[position2 - 1] = player2
