from sudoku.sudoku_solver import check_valid, check_solved, solve
class SudokuSpace:
    def __init__(self, original_value=' ', column_index=None, row_index=None):
        #print(f'SudokuSpace Init {column_index},{row_index}')
        self.column_index = column_index
        self.row_index = row_index

        # The assigned value
        self.original_value = original_value
        # The only possible options given the other values
        self.value_options = []
        # the current index of the current guess
        self.guess_index = 0
        # Fill this one when we're making a temporory guess
        self.temporary_guess = None
        # Final answer
        self.confident_guess = None


    def get_print_value(self):
        #TODO: Heirachry to get the printed thing. Original value, then confident guess, then temp guess.
        if self.original_value is not None and self.original_value != ' ':
            return self.original_value
        elif self.confident_guess is not None and self.confident_guess != ' ':
            return self.confident_guess
        elif self.temporary_guess is not None and self.temporary_guess != ' ':
            return self.temporary_guess
        else:
            return ' '

    def __eq__(self, otherSpace):
        return self.get_print_value() == otherSpace.get_print_value()

class SudokuBoard:
    def __init__(self):
        # Make a 2d array for easier indexing. Initialize with new objects.
        self.board = [[None for i in range(9)] for j in range(9)]
        for column_index in range(0,9):
            for row_index in range(0,9):
                self.board[column_index][row_index] = SudokuSpace(column_index=column_index, row_index=row_index)

    def is_valid(self):
        return check_valid(sudokuBoard=self)

    def is_solved(self):
        return check_solved(sudokuBoard=self)

    def solve(self, findAllPossible=False, printBoard=True):
        return solve(sudokuBoard=self, findAllPossible=findAllPossible, printBoard=printBoard)

    # This is the print method
    def __str__(self):
        boardToString = '\n'

        for rowIndex in range (0,9):
            # Add a divider character between boxes
            if (rowIndex in (3, 6)):
                boardToString += '------+-------+------\n'
            for columnIndex in range (0,9):
                cellValue = self.board[columnIndex][rowIndex].get_print_value()
                # Add a divider character between boxes
                if(columnIndex in (3,6)):
                    boardToString += '| '
                boardToString += str(cellValue)
                # Add a newline if we are at the end of the row.
                if(columnIndex == 8):
                    boardToString += '\n'
                else:
                    boardToString += ' '

        # Remove the last newLine character, don't need it.
        boardToString = boardToString[0:len(boardToString)-1]

        return boardToString


    def __eq__(self, otherBoard):
        # We are overwriting the equals method here. Just check that all 81 are equal.
        if(isinstance(otherBoard, SudokuBoard)):
            for column_index in range(0,9):
                for row_index in range(0,9):
                    if(self.board[column_index][row_index] != otherBoard.board[column_index][row_index]):
                        return False
            return True
        else:
            print('Warning: I cant compare a SudokuBoard with an object of type ' + str(type(obj)))
            return False