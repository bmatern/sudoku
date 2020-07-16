import random


class SudokuBoard:
    # It's just an array of integers. Length 81.
    board=[]
    solvedBoardList=[]

    def __init__(self):
        # Initialize the board with zeros.
        self.board=[0]*81
        self.solvedBoardList = []

    def isValid(self):
        # Validate the board. Return False if there are any obvious (duplicate integers, outside range) problems.
        # Check Rows, Columns, and the 3x3 boxes.
        return (self.isRowsValid() and self.isColumnsValid() and self.isBoxesValid())

    def isSolved(self):
        # If this board is valid, and none of them are zeroes, this is solved
        if(not self.isValid()):
            return False
        for boardValue in self.board:
            if boardValue not in [1,2,3,4,5,6,7,8,9]:
                #print('This board is NOT solved:\n' + str(self))
                return False
        #print('This board is solved!!:\n' + str(self))
        return True

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


    def solve(self, recursionDepth=None, findAllPossible=False):
        # Set the solved board list.
        if(recursionDepth is None):
            print('Please provide a recursion depth, or else I wont try to solve this.')
            self.solvedBoardList = []
            return
        elif(not self.isValid()):
            #print('This board is not valid, I cannot solve:\n' + str(self))
            self.solvedBoardList = []
            return
        else:
            #print('Solving board. Recursion Depth is ' + str(recursionDepth))
            #print(str(self))
            if (self.isSolved()):
                #print('This board is already solved! Returning this board.')
                self.solvedBoardList = [self]
                return

            else:
                # Try to solve this.
                # Find a random unsolved position.
                shuffledBoardIndices = list(range(81))
                random.shuffle(shuffledBoardIndices)
                boardIndex = -1
                for shuffledBoardIndex in shuffledBoardIndices:
                    if(self.board[shuffledBoardIndex] == 0):
                        boardIndex = shuffledBoardIndex
                        #print('Ill try to solve this board starting at position ' + str(boardIndex))
                        break

                # Loop: Assign 1-9 to this position.
                for guessValue in range(1,10):
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
                        #print('Success! found a solved puzzle at recursion depth ' + str(recursionDepth) + '!')
                        # Success, we found at least one solved puzzle.
                        if(findAllPossible):
                            #print('Extending the board list with a list of length ' + str(len(checkRecurseBoard.solvedBoardList)) + ' at recursion depth ' + str(recursionDepth) + '!')
                            self.solvedBoardList.extend(checkRecurseBoard.solvedBoardList)
                            # Not returning here because i want to check every possible puzzle.
                        else:
                            #print('Since one solution is enough I am just returning this single puzzle at recursion depth ' + str(recursionDepth) + '!')
                            #self.board=checkRecurseBoard.board
                            self.solvedBoardList = checkRecurseBoard.solvedBoardList
                            return



                        #if(findAllPossible and len(self.solvedBoardList) > 1):
                        #    print('I found a total of ' + str(len(self.solvedBoardList)) + ' Boards!')
                        #    return self.solvedBoardList

                #print('I tried every number 1-9 and this puzzle is unsolvable.')
                return

    def isRowsValid(self):
        for rowIndex in range(0, 9):
            #print('Checking row, indices are' + str(rowIndex*9) +' and ' + str((rowIndex*9)+9))
            rowToCheck = self.board[rowIndex*9 : (rowIndex*9)+9]
            if(not self.is9merValid(setToCheck=rowToCheck)):
                #print('No this row is not valid:' + str(rowToCheck))
                return False
        return True

    def isColumnsValid(self):
        for columnIndex in range(0, 9):
            columnToCheck = []
            for rowIndex in range(0, 9):
                cellIndex = rowIndex * 9 + columnIndex
                cellValue = self.board[cellIndex]
                columnToCheck.append(cellValue)

            #print('Checking column #' + str(columnIndex) + ', column is ' + str(columnToCheck))
            if (not self.is9merValid(setToCheck=columnToCheck)):
                #print('No this column is not valid:' + str(columnToCheck))
                return False
        return True

        return True

    def isBoxesValid(self):
        boxIndexList = [
            [0,1,2,9,10,11,18,19,20]
            ,[3,4,5,12,13,14,21,22,23]
            ,[6,7,8,15,16,17,24,25,26]
            ,[27,28,29,36,37,38,45,46,47]
            ,[30,31,32,39,40,41,48,49,50]
            ,[33,34,35,42,43,44,51,52,53]
            ,[54,55,56,63,64,65,72,73,74]
            ,[57,58,59,66,67,68,75,76,77]
            ,[60,61,62,69,70,71,78,79,80]
        ]
        for boxIndexList in boxIndexList:
            boxToCheck = [self.board[i] for i in boxIndexList]
            #print('Checking box' + str(boxToCheck))
            if(not self.is9merValid(boxToCheck)):
                #print('No this box is not valid:' + str(boxToCheck))
                return False

        return True

    def is9merValid(self, setToCheck=None):
        #print('Checking 9mer:' + str(setToCheck))

        # Are these 1-9s?
        for checkValue in setToCheck:
            if(type(checkValue) is not int):
                #print('Value ' + str(checkValue) + ' is not an integer, it is a ' + str(type(checkValue)))
                return False
            elif(checkValue not in [0,1,2,3,4,5,6,7,8,9]):
                #print('Value ' + str(checkValue) + ' is not okay, it should be 1-9 integer.')
                return False

        # strip out the zeroes, and check for duplicates
        strippedSet = [i for i in setToCheck if i != 0]
        #print('Zeroes Removed:' + str(strippedSet))
        # Check for Duplicates
        if (len(list(set(strippedSet))) != len(strippedSet)):
            #print('Duplicate values were removed, this set is not valid:' + str(setToCheck))
            return False

        # No duplicates, all are 1-9. Okay.
        #print('This set is valid:' + str(setToCheck))
        return True


    def __eq__(self, obj):
        # We are overwriting the equals method here. Just check that all 81 are equal.
        if(isinstance(obj, SudokuBoard)):
            for index, sudokuValue in enumerate(self.board):
                if(self.board[index] != obj.board[index]):
                    return False
            return True
        else:
            print('Warning: I cant compare a SudokuBoard with an object of type ' + str(type(obj)))
            return False

    def __str__(self):
        boardToString = ''
        for rowIndex in range (0,9):
            # Add a divider character between boxes
            if (rowIndex in (3, 6)):
                boardToString += '------+-------+------\n'
            for columnIndex in range (0,9):
                cellIndex = rowIndex * 9 + columnIndex
                cellValue = self.board[cellIndex]
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

    def copy(self):
        newObject = SudokuBoard()
        for index, value in enumerate(self.board):
            newObject.board[index]=value
        return newObject
