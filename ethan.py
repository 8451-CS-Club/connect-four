from gameboard import GameBoard
from time import sleep


def make_move(board):
    #Naive - place in the first open column
    for col in range(board.columns):
        if (board.check_valid(col, 'R')):
            print(col)
    exit(0)
    sleep(1)
    return (1)
