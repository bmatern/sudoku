from random import shuffle


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

    return True


def check_solved(sudokuBoard, performValidityCheck=True):
    print(f'checking if board is solved.\n{sudokuBoard}')

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


def assign_easy_cases(sudokuBoard):
    # Iterate and assign the easy cases. Rows then columns cuz we read a book that way.
    somethingWasChanged = False
    for rowIndex in range(0,9):
        for columnIndex in range(0,9):
            printValue = sudokuBoard.board[columnIndex][rowIndex].get_print_value()
            if printValue == ' ':
                potentialGuesses = assign_potential_guesses(sudokuBoard=sudokuBoard, column_index=columnIndex, row_index=rowIndex)

                # If there is only one option,
                if len(potentialGuesses) == 1:
                    #   assign it as a confident guess.
                    sudokuBoard.board[columnIndex][rowIndex].confident_guess = potentialGuesses[0]
                    somethingWasChanged = True
                # If there are zero options;
                elif len(potentialGuesses) == 0:
                    # Bail out. We're done, this is unsolvable.
                    print(f'No options possible at columnIndex={columnIndex} and rowIndex={rowIndex}')
                    return False

            else:
                pass
                #print(f'Value already assigned at columnIndex={columnIndex} and rowIndex={rowIndex}')

        # If we assign a confident guess
        # TODO: Do I need to check if it's still valid? Should be.

    # Start over the iteration if we changed something
    if somethingWasChanged:
        return assign_easy_cases(sudokuBoard=sudokuBoard)
    else:
        return True


def attempt_solve_first_position(sudokuBoard, printBoard=True):
    # find first open space (filter for those that were not originally or "confidently" solved)
    analysisCoordinates = None # Tuple of (columnIndex, rowIndex)

    for rowIndex in range(0,9):
        if analysisCoordinates is None:
            for columnIndex in range(0,9):
                if analysisCoordinates is None:
                    printValue = sudokuBoard.board[columnIndex][rowIndex].get_print_value()
                    if printValue == ' ':
                        analysisCoordinates = (columnIndex, rowIndex)

    #print(f'First empty position is at Column/Row:{analysisCoordinates}')
    if analysisCoordinates is None:
        # Apparently there are no unsolved spaces. Are we..done?
        if sudokuBoard.is_solved():
            return True
        else:
            raise Exception(f'Somehow we filled the board but it is not solved.\n{sudokuBoard}')

    columnIndex, rowIndex = analysisCoordinates

    # For each space assign all possibilities (they should be shuffled in this case)
    potentialGuesses = assign_potential_guesses(sudokuBoard=sudokuBoard, column_index=columnIndex, row_index=rowIndex)
    #print(f'At Column/Row:{analysisCoordinates} I see the options {potentialGuesses}')

    # If there are no options, Easy case. This is a fail.
    if len(potentialGuesses) < 1:
        return False

    # Loop through the options
    for guessIndex, guess in enumerate(potentialGuesses):
        #print(f'At Column/Row:{analysisCoordinates} I will guess a {guess} ({guessIndex+1}/{len(potentialGuesses)})')
        if printBoard:
            print(sudokuBoard)
        sudokuBoard.board[columnIndex][rowIndex].guess_index = guessIndex
        sudokuBoard.board[columnIndex][rowIndex].temporary_guess = guess

        # Is it valid?
        if sudokuBoard.is_valid():
            # Recursively check the next one.
            nextSubPositionWasSuccessful = attempt_solve_first_position(sudokuBoard=sudokuBoard, printBoard=printBoard)

            # If that was successful, we're done. We can return True.
            if nextSubPositionWasSuccessful:
                return True

            else:
                # Still more options at space?
                if guessIndex + 1 < len(potentialGuesses):
                    #print(f'At Column/Row:{analysisCoordinates} A zero based guess index of {guessIndex} is less than the length {len(potentialGuesses)} from options {potentialGuesses} so I will continue guessing.')
                    pass
                    # continue loop thru options
                # Otherwise
                else:
                    #print(f'At Column/Row:{analysisCoordinates} A zero based guess index of {guessIndex} was my last possible option for  {len(potentialGuesses)} from options {potentialGuesses} So I give up at this position and return False..')
                    # Reverse algorithm?
                    # Somehow take a step back
                    sudokuBoard.board[columnIndex][rowIndex].guess_index = None
                    sudokuBoard.board[columnIndex][rowIndex].temporary_guess = None
                    sudokuBoard.board[columnIndex][rowIndex].value_options = None
                    return False

        # Is it invalid? I think this should never happen.
        else:
            print(sudokuBoard)
            raise Exception(f'Somehow after guessing the board became invalid. At Column/Row:{analysisCoordinates} I guessed a {guess} ({guessIndex+1}/{len(potentialGuesses)}) from options {potentialGuesses}')

    return False


def solve(sudokuBoard, findAllPossible, printBoard=True):
    if printBoard:
        print('Solving Board:\n' + str(sudokuBoard))
    easyCaseWasSuccessful = assign_easy_cases(sudokuBoard=sudokuBoard)
    if not easyCaseWasSuccessful:
        return False

    # Is it solved? Then we're done
    # TODO: Store it in a set of possible solutions
    if sudokuBoard.is_solved():
        return True
        # TODO: Copy the board, store the confident guesses, and return it.


    # The second part of the solving algorithm, iterate through the unsolved spaces
    firstPositionWasSuccessful = attempt_solve_first_position(sudokuBoard=sudokuBoard, printBoard=printBoard)

    # Is it solved? Then we're done
    # TODO: Store it in a set of possible solutions
    if sudokuBoard.is_solved():
        return True
        # TODO: Copy the board, store the confident guesses, and return it.
    else:
        raise Exception('I could not solve the board. Do something about it, maybe return false or something')

def get_box_id(columnIndex, rowIndex):
    #[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]# TOP LEFT
    if columnIndex in range(0,3) and rowIndex in range(0,3):
        return 0
    #(3,0),(3,1),(3,2),(4,0),(4,1),(4,2),(5,0),(5,1),(5,2)]# TOP MID
    elif columnIndex in range(3,6) and rowIndex in range(0,3):
        return 1
    #[(6,0),(6,1),(6,2),(7,0),(7,1),(7,2),(8,0),(8,1),(8,2)]# TOP RIGHT
    elif columnIndex in range(6,9) and rowIndex in range(0,3):
        return 2
    #[(0,3),(0,4),(0,5),(1,3),(1,4),(1,5),(2,3),(2,4),(2,5)]# MID LEFT
    elif columnIndex in range(0,3) and rowIndex in range(3,6):
        return 3
    #[(3,3),(3,4),(3,5),(4,3),(4,4),(4,5),(5,3),(5,4),(5,5)]# MID MID
    elif columnIndex in range(3,6) and rowIndex in range(3,6):
        return 4
    #[(6,3),(6,4),(6,5),(7,3),(7,4),(7,5),(8,3),(8,4),(8,5)]# MID RIGHT
    elif columnIndex in range(6,9) and rowIndex in range(3,6):
        return 5
    #[(0,6),(0,7),(0,8),(1,6),(1,7),(1,8),(2,6),(2,7),(2,8)]# BOTTOM LEFT
    elif columnIndex in range(0,3) and rowIndex in range(6,9):
        return 6
    #[(3,6),(3,7),(3,8),(4,6),(4,7),(4,8),(5,6),(5,7),(5,8)]# BOTTOM MID
    elif columnIndex in range(3,6) and rowIndex in range(6,9):
        return 7
    #[(6,6),(6,7),(6,8),(7,6),(7,7),(7,8),(8,6),(8,7),(8,8)]# BOTTOM RIGHT
    elif columnIndex in range(6,9) and rowIndex in range(6,9):
        return 8

    raise Exception(f'Could not find box id for columnIndex={columnIndex} and rowIndex={rowIndex}')




def assign_potential_guesses(sudokuBoard, column_index, row_index):
    rowValues = set([sudokuBoard.board[columnIndex][row_index].get_print_value() for columnIndex in range(0,9)])
    #print(f'row {row_index} contains these values:{rowValues}')


    columnValues = set([sudokuBoard.board[column_index][rowIndex].get_print_value() for rowIndex in range(0,9)])
    #print('column ' + str(column_index) + ' contains these values:' + str(columnValues))

    # Remove Box values
    boxIndex = get_box_id(columnIndex=column_index, rowIndex=row_index)
    boardIndices = get_boxes(boxIndex=boxIndex)[0] # Index 0 because this method returns a list of lists.
    boxValues = set([sudokuBoard.board[columnIndex][rowIndex].get_print_value() for columnIndex, rowIndex in boardIndices])
    #print('boxIndex ' + str(boxIndex) + ' has these box values: ' + str(boxValues))

    potentialGuesses = list({'1','2','3','4','5','6','7','8','9'}.difference(rowValues).difference(columnValues).difference(boxValues))
    shuffle(potentialGuesses)
    #print('So I am left with' + str(potentialGuesses))

    sudokuBoard.board[column_index][row_index].value_options = potentialGuesses
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

def get_boxes(boxIndex=None):
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
    if boxIndex is None:
        return boxIndexList
    else:
        # If a boardIndex was provided, we can provide a single box.
        # This is the box containing the provided boardIndex.
        # What was the purpose of this? Oh yeah; when i am checking possible values, I should check within the correct b ox.
        # TODO: This is still a list of length 1. To be consistent in the return value.
        return [boxIndexList[boxIndex]]

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