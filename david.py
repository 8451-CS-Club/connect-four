import operator


def make_move(board, color):

    score_dict = {}

    for col in range(board.columns):
        board_copy = board
        score = get_proximity_score(board_copy, col, color)
        score_dict[col] = score

    highest_score = max(score_dict.items(), key=operator.itemgetter(1))[0]
    print(score_dict)
    return highest_score + 1


def get_proximity_score(board_copy, col, color):

    score = 0

    # loop through board to evaluate every spot
    for y in range(board_copy.rows):
        for x in range(col-2, col+2):
            # Evaluate if the spot has my color piece within 2 spaces away
            for yprox in range(-2, 3):
                for xprox in range(-2, 3):
                    try:
                        if (0 < y+yprox < 6) and (board_copy.board[y + yprox][x + xprox] == color):
                            score += 50
                    except IndexError:
                        score += 0

    return score
