class GameBoard:

    def __init__(self, columns=6, rows=7):
        self.columns = columns
        self.rows = rows
        self.board = [[' ' for x in range(self.rows)] for y in range(self.columns)]


    def print_board(self):
        '''
        used to display the current state of the board
        '''
        for row in self.board:
            print(*row, sep=' | ')


    def place_piece(self, x, y, color):
        '''
        method to place a piece into the board.
        '''

        # Take one off of each value to account for zero indexes
        x = x - 1
        y = y - 1

        # input checks
        if x > 6 or x < 0:
            print("X must be in between 1 and 7")
        if y > 5 or y < 0:
            print("Y must be in between 1 and 6")
        if color != 'R' and color != 'Y':
            print("Color must be either R or Y")

        # Be sure there's already a piece below it
        if y + 1 < 6:
            if self.board[y+1][x] == ' ':
                print("That's not a valid spot.")

        # Be sure the spot isn't taken and place the piece
        if self.board[y][x] == ' ':
            self.board[y][x] = color
        else:
            print("That spot is already taken!")


    def check_for_winner(self, color):

        # check horizontal
        for x in range(self.columns - 3):
            for y in range(self.rows - 3):
                if self.board[y][x] == color \
                and self.board[y][x+1] == color \
                and self.board[y][x+2] == color:
                    print("you won!")
                    return True

        # check vertical
        for y in range(self.rows - 3):
            for x in range(self.columns - 3):
                if self.board[y][x] == color \
                and self.board[y+1][x] == color \
                and self.board[y+2][x] == color:
                    print("you won!")
                    return True
