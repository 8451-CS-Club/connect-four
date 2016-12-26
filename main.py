from gameboard import GameBoard
import player1 as p1
import player1 as p2
import time


#Note: P1 is red, P2 is yellow


def game_loop():

    board = GameBoard() #initialize a board
    winner = None #initialize the winner variable
    n_turns = 0 #initialize the turn count

    #Run the game - looping until someone wins
    while (winner == None):
        board.print_board()
        
        #Figure out the current player and color
        if (n_turns % 2): #if there have been an odd number of turns
            player = p2 #P2 makes the next move
            color = 'Y' #and the color is yellow
        else: #if there have been an even number of moves...you get it
            player = p1
            color = 'R'

        #Loop until valid input
        is_valid = False
        while (not is_valid):
            x,y = player.make_move(board) #call the player's move function 
            is_valid = board.check_valid(x, y, color)

	#Place the piece and check for a winner
        board.place_piece(x, y, color)
        winner = board.check_for_winner(color)

#Driver
if __name__ == '__main__':
    game_loop()
