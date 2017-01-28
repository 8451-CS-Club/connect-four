from gameboard import GameBoard
from time import sleep
import copy


def make_move(board, color):
    best_move_x = 0
    best_val = -2 #This value being lower than -1 means the player will prefer an empty space over nothing, even if it means losing
    for x in range(board.columns):
        print("looping on x: ",x)
        open_y = open_row(board, x)
        print(open_y)
        if (open_y == -1):
            #only keep this value if we haven't found an open space yet
            if (best_val == -2):
                best_move_x = x
            continue
        new_board = copy.deepcopy(board)
        new_board.board[open_y][x] = color
        #new_board.print_board()
        current_val = board_val(new_board, color)
        if (current_val > best_val):
            print("updating best move")
            best_val = current_val
            best_move_x = x
        print("finished looping on x: ", x)
    return(best_move_x + 1) #account for the "human" indexing of the board

# Recursive function to figure out who will win in
# this situation given optimal play
def board_val(board, color):
    board_val.counter += 1
    if (not (board_val.counter % 1000)):
        print(board_val.counter)
    # Exit conditions first
    winner = board.check_for_winner(color)
    if (winner == color):
        return 1
    elif (winner is not None):
        return -1
    else:
        max_opp_board_val = -1
        opp_move_x = -1
        opp_move_y = -1
        for x in range(board.columns):
            #Find the first open spot in that column
            open_y = open_row(board, x)
            if (open_y == -1):
                continue #skip to the next column
            opp_color = 'R' if (color == 'Y') else 'Y' #concisely get opponent's color
            #create a new board with an opponent's piece there
            new_board = copy.deepcopy(board)
            new_board.board[open_y][x] = opp_color
            #Calculate this board's value to your opponent
            current_board_val = board_val(new_board, opp_color)
            # If you find a board where your opponent always wins
            if (current_board_val == 1):
                return(-1) # then you always lose (duh)
            #Otherwise, if it's the best one you've found for your opponent, remember it
            if current_board_val > max_opp_board_val:
                max_opp_board_val = current_board_val
                opp_move_y = open_y
                opp_move_x = x
        # Now that we've checked all the columns, we know the best move for our opponent
        # Return the opposite value of that move's value to her
        return(-1 * max_opp_board_val)

board_val.counter = 0

# Get the first open row in a column
# Return -1 if no opening
def open_row(board, column):
    if (column >= board.columns or column < 0):
        print("Error, invalid column specified")
        exit(1)
    for y in reversed(range(board.rows)):
        if (board.board[y][column] == " "):
            return y
    return -1 #if there aren't any openings, return -1
