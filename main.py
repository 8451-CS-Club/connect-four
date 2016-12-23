from gameboard import GameBoard
from player1 import make_move


def game_loop():

    board = GameBoard()
    winner = False
    while (winner == False):
        make_move(board)
        board.print_board()
        print(board.check_for_winner)

if __name__ == '__main__':
    game_loop()
