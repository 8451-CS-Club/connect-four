from gameboard import GameBoard
from time import sleep
import copy

# Make a move
def make_move(board, color):
    best_move_x = 0
    # This value being lower than -1 means the player will prefer an
    # empty space over nothing, even if it means losing
    best_val = -2 
    return(find_best_move(board, color))


# Find the best move for a player given a current board state
def find_best_move(board, color):
    # Initialize the best move value at -2 because even a losing
    # move (with a value of -1) is better than doing nothing (-2)
    best_move_value = -2
    best_move_col = -1
    # Check the value of placing a piece in each column
    for x in range(board.columns):
        # Get the x-coordinate of where a piece would be placed
        y = open_row(board, x)
        # If the row is full, skip to next loop iteration
        if y == -1:
            continue
        # If the row is not full, record that it is a viable move location
        else:
            last_valid_move = x

        # Copy the board and add a piece in the correct position
        hypothetical_board = board.copy()
        hypothetical_board.board[y][x] = color
        # Get the value of the board resulting from placing a pice here
        hypothetical_value = board_val(hypothetical_board, color)
        # If this move has a value of 1 (a win for the player), return it
        if hypothetical_value == 1:
            return x
    
    # If there weren't any moves that result in a win, just return the last
    # valid move found
    return(last_valid_move)


# Recursive function to figure out who will win in
# this situation given that the opponent moves next
def board_val(board, color):
    print("modeling the value of this board: ")
    board.print_board()
    print("to " + color)
    # Run a counter so we can track how much this runs
    board_val.counter += 1
    if (not (board_val.counter % 100)):
        print(board_val.counter)
    # Concisely get opponent's color
    opp_color = 'R' if (color == 'Y') else 'Y'

    # Exit conditions first
    winner = board.check_for_winner()
    if (winner == color):
        print("found that I win")
        return 1
    elif (winner == opp_color):
        print("found that you win")
        return -1
    else:
        max_opp_board_val = -1
        opp_move_x = -1
        opp_move_y = -1

        # Determine the value of the board that will result after opponent
        # makes her optimal move
        opp_move = find_best_move(board, opp_color)
        # Create a board and add this opponent move
        opp_move_board = board.copy() 
        opp_y_pos = open_row(opp_move_board, opp_move)
        opp_move_board.board[opp_y_pos][opp_move] = opp_color
        # Return the oppositve of the value of this board to your opponent
        return -1 * board_val(opp_move_board, opp_color)

# Counter for how many times this function is called
board_val.counter = 0


# Get the first open row in a column
# Return -1 if the column is full
# TESTED AND COMPLETED
def open_row(board, column):
    if (column >= board.columns or column < 0):
        print("Error, invalid column specified")
        exit(1)
    for y in range(board.rows):
        if (board.board[y][column] == " "):
            return y
    return -1 #if there aren't any openings, return -1
