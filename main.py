from gameboard import GameBoard
import player1


def game_loop():

    board = GameBoard()
    winner = False
    while (winner == False):
        move_status = player1.make_move(board)
        if move_status == False:
            break
        board.print_board()
        winner = board.check_for_winner('R')

if __name__ == '__main__':
    game_loop()
