#from board import SudokuBoard


def check_valid(sudokuBoard):
    #print('Checking if board is valid.')

    # Validate the board. Return False if there are any obvious (duplicate integers, outside range) problems.
    # Check Rows, Columns, and the 3x3 boxes.
    #

    # Another option. For each position loop and find potential values.
    # If that's less than 1, the board is impossible.

    # TODO: Yeah I probably want to re-add this at some point, check each position, if there are zero possibilities then it's unsolvable.
    #   This is probably better than checking all the rows and columns and boxes..
    #for boardIndex, boardValue in enumerate(self.board):
    #    if(len(self.getPotentialGuesses(boardIndex)) < 1):
    #        return False

        #if(boardValue==0 and len(self.getPotentialGuesses(boardIndex)) < 1):
        #    #print('Not possible to have place anything at position ' + str(boardIndex) + ' on  board:\n' + str(self))
        #    return False
    if not is_rows_valid(sudokuBoard=sudokuBoard):
        return False
    if not is_columns_valid(sudokuBoard=sudokuBoard):
        return False
    if not  is_boxes_valid(sudokuBoard=sudokuBoard):
        return False


def check_solved(sudokuBoard, performValidityCheck=True):
    #print('checking if board is solved.')

    # If this board is valid, and none of them are zeroes, this is solved
    if(not check_valid(sudokuBoard=sudokuBoard)):
        return False
    for columnIndex in range(0,9):
        for rowIndex in range(0,9):
            boardValue = sudokuBoard.board[columnIndex][rowIndex].get_print_value()
            if boardValue not in ['1','2','3','4','5','6','7','8','9']:
                #print('This board is NOT solved:\n' + str(self))
                return False
    #print('This board is solved!!:\n' + str(self))
    return True


def solve(sudokuBoard, findAllPossible):
    print('Solving Board:\n' + str(sudokuBoard))

    # Iterate and assign the easy cases.  If there is only one option, assign it as a confident guess.
        # If there are zero options;
            # Bail out. We're done, this is unsolvable.

        # If we assign a confident guess
            # Each case check if it's still valid

            # Start over the iteration if we changed something

    # Is it solved? Then we're done
    if sudokuBoard.is_solved():
        return True

    else:
        raise Exception('I need to implement the second half of the solving algorightm')

    # For each space assign all possibilities (they should be shuffled in this case)

    # Start a solving loop

        # forward portion (probably a separate method

            # Get the first unfilled space (filter for those that were not originally or "confidently" solved)

            # Loop through the options

                #

        # backward portion





    '''
    print('Original Board = ' + str(self.originalBoard))
    if (not self.isValid()):
        print('This board is not valid, I cannot solve:\n' + str(self))
        return None
    elif (self.isSolved()):
        print('This board is already solved! Returning this board.')
        self.solvedBoardList.append(self.board)
        return self

    else:
        print('I will attempt to solve...')

        # Calculate Possibilities for each position
        for currentPositionIndex in range(0,81):
            #print('Checking position ' + str( currentPositionIndex))
            self.potentialOptions[currentPositionIndex] = self.getPotentialGuesses(boardIndex=currentPositionIndex)

        currentPositionIndex=0
        # Loop All position indices
        while(currentPositionIndex <= 80 and currentPositionIndex >= 0):
            print('At position ' + str(currentPositionIndex) + ' there are these options:' + str(self.potentialOptions[currentPositionIndex]))

            # Loop Possibilities
            for possibleValue in sorted(list(self.potentialOptions[currentPositionIndex])):
                print('Guessing ' + str(possibleValue) + ' at position ' + str(currentPositionIndex))
                self.board[currentPositionIndex] = possibleValue

                if(not self.isValid()):
                    print(str(possibleValue) + ' at position ' + str(currentPositionIndex) + ' did not work.')
                    self.board[currentPositionIndex] = 0
                    continue

                elif(self.isSolved()):
                    print('I found a solved board:\n' + str(self))
                    self.solvedBoardList.append(self.board)
                    if(findAllPossible):
                        print('I will continue and see if there are more solutions.')
                    else:
                        print('All done.')
                        currentPositionIndex=-1
                        break

                #else:
                # If it's valid then maybe I can increment the position and continue.


                # If Solved, add to solvedBoardList
                # If valid
                # If Invalid pass

            currentPositionIndex += 1
            
    '''


def getPotentialGuesses(self, boardIndex=None):

    if (self.board[boardIndex] != 0):
        return {self.board[boardIndex]}

    rowIndex = boardIndex // 9
    rowValues = set([self.board[i] if i!=boardIndex else 0 for i in [i + rowIndex*9 for i in range(0,9)]])
    #print('row ' + str(rowIndex) + ' contains these values:' + str(rowValues))

    columnIndex = boardIndex % 9
    columnValues = set([self.board[i] if i!=boardIndex else 0 for i in [i*9 + columnIndex for i in range(0,9)]])
    #print('column ' + str(columnIndex) + ' contains these values:' + str(columnValues))

    # Remove Box values
    boxIndices = self.getBoxes(boardIndex=boardIndex)
    boxValues = set([self.board[i] if i!=boardIndex else 0 for i in boxIndices])
    #print('boardIndex ' + str(boardIndex) + ' has these box values: ' + str(boxValues))

    potentialGuesses = set(range(1,10)).difference(rowValues).difference(columnValues).difference(boxValues)
    #print('So I am left with' + str(potentialGuesses))
    return potentialGuesses

def is_rows_valid(sudokuBoard):
    for rowIndex in range(0, 9):
        rowToCheck = [sudokuBoard.board[columnIndex][rowIndex].get_print_value() for columnIndex in range(0,9)]
        #print(f'Row {rowIndex} has values {rowToCheck}')
        if(not is_9mer_valid(setToCheck=rowToCheck)):
            #print('No this row is not valid:' + str(rowToCheck))
            return False
    return True

def is_columns_valid(sudokuBoard):
    for columnIndex in range(0, 9):
        columnToCheck = [sudokuBoard.board[columnIndex][rowIndex].get_print_value() for rowIndex in range(0,9)]
        #print(f'Column {columnIndex} has values {columnToCheck}')
        if (not is_9mer_valid(setToCheck=columnToCheck)):
            #print('No this column is not valid:' + str(columnToCheck))
            return False
    return True
def is_boxes_valid(sudokuBoard):
    boxIndexList = get_boxes()
    for boxIndex in range(0,len(boxIndexList)):
        boxToCheck = [sudokuBoard.board[columnIndex][rowIndex].get_print_value() for columnIndex, rowIndex in boxIndexList[boxIndex]]
        #print('Checking box' + str(boxToCheck))
        if(not is_9mer_valid(setToCheck=boxToCheck)):
            #print('No this box is not valid:' + str(boxToCheck))
            return False
    return True

def get_boxes(boardIndex = None):
    # TODO: This is allocated many times. I should allocate it once and pass it around..
    boxIndexList = [
        [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]# TOP LEFT
        ,[(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)]# TOP MID
        ,[(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)]# TOP RIGHT
        ,[(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]# MID LEFT
        ,[(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)]# MID MID
        ,[(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)]# MID RIGHT
        ,[(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)]# BOTTOM LEFT
        ,[(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)]# BOTTOM MID
        ,[(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]# BOTTOM RIGHT
    ]
    if boardIndex is None:
        return boxIndexList
    else:
        # If a boardIndex was provided, we can provide a single box.
        # This is the box containing the provided boardIndex.
        # What was the purpose of this? Oh yeah; when i am checking possible values, I should check within the correct b ox.
        for boxIndex in boxIndexList:
            if(boardIndex in boxIndex):
                return boxIndex

def is_9mer_valid(setToCheck=None):
    #print('Checking 9mer:' + str(setToCheck))
    # Are these 1-9s?
    try:
        # TODO: Do i need to filter out None or something here?
        for checkValue in setToCheck:
            if(checkValue not in [' ', '1','2','3','4','5','6','7','8','9']):
                print('Value ' + str(checkValue) + ' is not okay, it should be 1-9 integer.')
                return False
        # check for duplicates. TODO: Excluding the spaces which are not yet solved.
        strippedSet = [i for i in setToCheck if i != ' ']
        #print('Zeroes Removed:' + str(strippedSet))
        # Check for Duplicates
        if (len(list(set(strippedSet))) != len(strippedSet)):
            print('Duplicate values were removed, this set is not valid:' + str(setToCheck))
            return False

        # No duplicates, all are 1-9. Okay.
        #print('This set is valid:' + str(setToCheck))
        return True


    except Exception as error:
        print(f'Exception checking is 9emer valid for set {setToCheck}:{error}')
        return False