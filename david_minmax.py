from gameboard import GameBoard


def make_move(board, n_turns, color):

    '''
    Minimax algorithm:
        -simulate every possible move for my player
        -then simulate every move after that for my opponent
        -continue this for as long as the depth parameter is > 0
        -once it's 0, all moves should be scored and the largest should be chosen
        -a winning move for me is a score of 1000
        -a winning move for opponent is -1000
    '''

    depth = 5



def get_possible_moves(board, color):

    for col in range(board.columns):
        board_copy = board.place_piece(col, color)
        score = MinMax(board_copy, player, depth + 1, max_depth)


def evaluate_score(board, color):

    if board.check_for_winner(color) == color:
        return 1000


def get_proximity_score(board, col, color):
    '''
    returns a score based on how close my own pieces are
    bonus if they are touching
    '''
    proximity_pieces = 0
    proximity_y_values = [-2, -1, 0, 1, 2]
    proximity_x_values = [-1, 0, 1]

    score = 0

    board.place_piece(2, color)
    board.print_board()

    # loop through board to evaluate every spot
    for y in range(board.rows):
        for x in range(board.columns):
            # Evaluate if the spot has my color piece within 2 spaces away
            for yprox in range(-2, 3):
                for xprox in range(-2, 3):
                    try:
                        if (y+yprox > 0 and y+yprox < 6) and (board.board[y + yprox][x + xprox] == color):
                            board.place_piece(x+xprox, color)
                            print("expected match sport")
                            board.print_board()
                            score += 50
                    except IndexError:
                        score += 0

    return score
