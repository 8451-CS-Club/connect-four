class GameBoard:

    def __init__(self, columns=7, rows=6):
        self.columns = columns
        self.rows = rows
        self.board = [[' ' for x in range(self.columns)] for y in range(self.rows)]


    def print_board(self):
        '''
        used to display the current state of the board
        '''
        for row in self.board:
            print(*row, sep=' | ')


    def check_valid(self, x, y, color):
        '''
        Method to check that a spot is valid
	Returns True if valid, False if not
        '''
        # Take one off of each value to account for zero indexes
        x = x - 1
        y = y - 1

        # Check that it's on the board
        if x >= self.columns  or x < 0:
            print("X must be in between 1 and 6")
            return False
        if y >= self.rows or y < 0:
            print("Y must be in between 1 and 7")
            return False
        if color != 'R' and color != 'Y':
            print("Color must be either R or Y")
            return False

        # Be sure there's already a piece below it
        if y + 1 < 6:
            if self.board[y+1][x] == ' ':
                print("That's not a valid spot.")
                return False

        # Be sure the spot isn't taken and place the piece
        if self.board[y][x] != ' ':
            print("That spot is already taken!")
            return False

        #If you pass all these tests, return true
        return True
        


    def place_piece(self, x, y, color):
        '''
        method to place a piece into the board.
        '''

        # Take one off of each value to account for zero indexes
        x = x - 1
        y = y - 1

        self.board[y][x] = color


    def check_for_winner(self, color):

        # check horizontal
        for x in range(self.columns - 3):
            for y in range(self.rows - 3):
                if self.board[y][x] == color \
                and self.board[y][x+1] == color \
                and self.board[y][x+2] == color:
                    print(color + " wins!")
                    return color

        # check vertical
        for y in range(self.rows - 3):
            for x in range(self.columns - 3):
                if self.board[y][x] == color \
                and self.board[y+1][x] == color \
                and self.board[y+2][x] == color:
                    print(color + " wins!")
                    return color

        return None
