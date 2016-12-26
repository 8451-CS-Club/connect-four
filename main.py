from gameboard import GameBoard
import player1 as p1
import player1 as p2
import time


#Note: P1 is red, P2 is yellow


def game_loop():

    board = GameBoard()
    winner = None
    n_turns = 0
    while (winner == None):
        board.print_board()
        
        #Loop until valid input
        is_valid = False

        #Figure out the current player and color
        if (n_turns % 2): #if there have been an odd number of turns
            player = p2
            color = 'Y'
        else:
            player = p1
            color = 'R'
        while (not is_valid):
            x,y = player.make_move(board) #P2 makes the next move
            is_valid = board.check_valid(x, y, color)

        board.place_piece(x, y, color)
        winner = board.check_for_winner(color)
        time.sleep(1)

if __name__ == '__main__':
    game_loop()
