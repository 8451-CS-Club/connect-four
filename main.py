from gameboard import GameBoard
import player1


def game_loop():

    board = GameBoard()
    winner = None
    while (winner == None):
        board.print_board()
        
        #Loop until valid input
        is_valid = False
        while (not is_valid):
            x,y = player1.make_move(board)
            is_valid = board.check_valid(x, y, 'R')
          
        board.place_piece(x, y, 'R')
        winner = board.check_for_winner('R')

if __name__ == '__main__':
    game_loop()
