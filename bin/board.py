from bin.sudoku_solver import check_valid, check_solved, solve
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
        # TODO: Heirachry to get the printed thing. Original value, then confident guess, then temp guess.
        return self.original_value

    def __eq__(self, otherSpace):
        return self.get_print_value() == otherSpace.get_print_value()

class SudokuBoard:
    def __init__(self):
        # Make a 2d array for easier indexing. Initialize with new objects.
        self.board = [[None for i in range(9)] for j in range(9)]
        for column_index in range(0,9):
            for row_index in range(0,9):
                self.board[column_index][row_index] = SudokuSpace(column_index=column_index, row_index=row_index)

    def set_original(self, original_value, column_index, row_index):
        self.board[column_index][row_index].original_value = original_value

    def get_original(self, column_index, row_index):
        return self.board[column_index][row_index].original_value

    def is_valid(self):
        return check_valid(sudokuBoard=self)

    def is_solved(self):
        return check_solved(sudokuBoard=self)

    def solve(self, findAllPossible=False):
        solve(sudokuBoard=self, findAllPossible=findAllPossible)

    '''
    # Not necessary because I think my algorithm prevents duplicate solutions.
    def removeDuplicateSolvedBoards(self):
        # NOT working. Need to loop backwards and remove these.
        # Are there duplicates possible with my algorithm? I don't know actually, maybe it's not possible
        # I think this will at least detect duplicates.
        for leftIndex, leftSolvedBoard in enumerate(self.solvedBoardList):
            for rightIndex, rightSolvedBoard in enumerate(self.solvedBoardList):
                if (leftIndex != rightIndex):
                #if (True):
                    #print('Comparing board ' + str(leftIndex) + ' with board ' + str(rightIndex))
                    if(leftSolvedBoard == rightSolvedBoard):
                        print('These two are identical!:\n' + str(leftSolvedBoard) + '\n\n' + str(rightSolvedBoard))
    '''
    '''
    def solve(self, recursionDepth=None, findAllPossible=False):
        # Set the solved board list.
        if(recursionDepth is None):
            print('Please provide a recursion depth, or else I wont try to solve this.')
            self.solvedBoardList = []
            return None
        elif(not self.isValid()):
            #print('This board is not valid, I cannot solve:\n' + str(self))
            self.solvedBoardList = []
            return None
        elif (self.isSolved()):
                #print('This board is already solved! Returning this board.')
                self.solvedBoardList = [self]
                return self

        else:
            # Try to solve this.
            print('Solving board. Recursion Depth is ' + str(recursionDepth))
            #print(str(self))
            boardIndex = self.getRandomUnsolvedBoardPosition()

            # Loop: Assign 1-9 to this position.
            # Actually I can exclude some. Maybe this saves time, I dont have to copy the board for each guess that is impossible.
            guessValues = self.getPotentialGuesses(boardIndex=boardIndex)

            for guessValue in guessValues:
                #print('Checking if a value of ' + str(guessValue) + ' will work at position ' + str(boardIndex))
                checkRecurseBoard = self.copy()
                checkRecurseBoard.board[boardIndex] = guessValue

                #Try solving it
                #print('Puzzle is still valid, I will try solving it...')
                checkRecurseBoard.solve(recursionDepth=recursionDepth+1, findAllPossible=findAllPossible)
                if(checkRecurseBoard.solvedBoardList is None or len(checkRecurseBoard.solvedBoardList) < 1):
                    #print('RecursedSolvedBoardList is Empty. I didnt find anything.')
                    pass
                else:
                    print('Success! found ' + str(len(checkRecurseBoard.solvedBoardList)) + ' solved puzzle at recursion depth ' + str(recursionDepth) + '!')
                    # Success, we found at least one solved puzzle.
                    if(findAllPossible):
                        #print('Extending the board list with a list of length ' + str(len(checkRecurseBoard.solvedBoardList)) + ' at recursion depth ' + str(recursionDepth) + '!')
                        self.solvedBoardList.extend(checkRecurseBoard.solvedBoardList)
                        # Not returning here because i want to check every possible puzzle.
                    else:
                        #print('Since one solution is enough I am just returning this single puzzle at recursion depth ' + str(recursionDepth) + '!')
                        self.board=checkRecurseBoard.board
                        self.solvedBoardList = checkRecurseBoard.solvedBoardList
                        return self



                    #if(findAllPossible and len(self.solvedBoardList) > 1):
                    #    print('I found a total of ' + str(len(self.solvedBoardList)) + ' Boards!')
                    #    return self.solvedBoardList

            #print('I tried every number 1-9 and this puzzle is unsolvable.')
            return None

    def getRandomUnsolvedBoardPosition(self):
        # Find a random unsolved position. Return a -1 if I can't find one.
        shuffledBoardIndices = list(range(81))
        random.shuffle(shuffledBoardIndices)
        boardIndex = -1
        for shuffledBoardIndex in shuffledBoardIndices:
            if (self.board[shuffledBoardIndex] == 0):
                boardIndex = shuffledBoardIndex
                # print('Ill try to solve this board starting at position ' + str(boardIndex))
                break
        return boardIndex
        
    '''


    # This is the print method
    def __str__(self):
        boardToString = ''

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