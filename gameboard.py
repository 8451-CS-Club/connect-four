class GameBoard:

    def __init__(self, columns=7, rows=6):
        self.columns = columns
        self.rows = rows
        self.board = [[' ' for x in range(self.columns)] for y in range(self.rows)]


    def print_board(self):
        '''
        used to display the current state of the board
        '''
        print("   -", end="") #spacer
        print("-" * 4 * self.columns)

        # Print row numbers and the board itself
        for rownum, row in reversed(list(enumerate(self.board))):
            print(str(rownum) + "  | ", end = "") #print the row number
            print(*row, sep=' | ', end = "") #print the row
            print(" |\n", end = "")

        # Print column numbers
        print("   -", end="") #spacer
        print("-" * 4 * self.columns)
        print("     ", end="")
        print(*[x for x in range(self.columns)], sep = '   ')

        print("\n\n")


    def check_valid(self, col, color):
        '''
        Method to check that a spot is valid
	Returns True if valid, False if not
        '''
        # Take one off of the input value to account for zero indexes
        col = col

        # Check that it's on the board
        if col >= self.columns  or col < 0:
            print("Column number must be in between 0 and " + str(self.columns))
            return False
        #Check if the color is valid
        if color not in ('R','Y'):
            print("Color must be either R or Y")
            return False

        # Find the first open spot in that column
        col_is_full = True
        for y in reversed(range(self.rows)):
            if self.board[y][col] == ' ': #If that spot is empty
                col_is_full = False #Note that there is space for the piece
                break #stop looping

        if col_is_full == True:
            print("That column is full")
            return False

        #If you pass all these tests, return true
        return True



    def place_piece(self, col, color):
        '''
        method to place a piece into the board.
        '''

        # Find the first open spot in that column
        for y in range(self.rows):
            if self.board[y][col] == ' ': #If that spot is empty
                self.board[y][col] = color #Place the piece
                break #stop looping


    def check_for_winner(self, color):

        # check horizontal
        for x in range(self.columns - 3):
            for y in range(self.rows):
                if self.board[y][x] == color \
                and self.board[y][x+1] == color \
                and self.board[y][x+2] == color \
                and self.board[y][x+3] == color:
                    return color

        # check vertical
        for y in range(self.rows - 3):
            for x in range(self.columns):
                if self.board[y][x] == color \
                and self.board[y+1][x] == color \
                and self.board[y+2][x] == color \
		and self.board[y+3][x] == color:
                    return color

        # check diagonal (top right to bottom left)
        for y in range(self.rows - 3):
            for x in range(self.columns - 3):
                if self.board[y][x+3] == color \
                and self.board[y+1][x+2] == color \
                and self.board[y+2][x+1] == color \
                and self.board[y+3][x] == color:
                    return color

        # check diagonal (top left to bottom right)
        for y in range(self.rows - 3):
            for x in range(self.columns - 3):
                if self.board[y][x] == color \
                and self.board[y+1][x+1] == color \
                and self.board[y+2][x+2] == color \
                and self.board[y+3][x+3] == color:
                    return color

        # Last, check to see if the board is full even though
        # there was no winner (a stalemate)
        cells = [self.board[y][x] for x in range(self.columns)
                                  for y in range(self.rows)]
        # If there are no blank spaces left...
        if ' ' not in cells:
            return(' ')

        # If none of the above conditions are met, nothing
        # interesting has happened
        return None


    # Create a copy of the current board and return it
    def copy(self):
        new_board = GameBoard(self.columns, self.rows)
        for x in range(self.columns):
            for y in range(self.rows):
                new_board.board[y][x] = self.board[y][x]
        return(new_board) 
