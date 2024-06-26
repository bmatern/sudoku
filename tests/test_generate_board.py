from pytest import fixture
from copy import deepcopy

from bin.board import SudokuBoard


@fixture()
def solved_board():
    solvedBoard = SudokuBoard()
    solvedBoard.set_original(original_value='1', column_index=0, row_index=0)
    solvedBoard.set_original(original_value='2', column_index=1, row_index=0)
    solvedBoard.set_original(original_value='3', column_index=2, row_index=0)
    solvedBoard.set_original(original_value='4', column_index=3, row_index=0)
    solvedBoard.set_original(original_value='5', column_index=4, row_index=0)
    solvedBoard.set_original(original_value='6', column_index=5, row_index=0)
    solvedBoard.set_original(original_value='7', column_index=6, row_index=0)
    solvedBoard.set_original(original_value='8', column_index=7, row_index=0)
    solvedBoard.set_original(original_value='9', column_index=8, row_index=0)
    solvedBoard.set_original(original_value='4', column_index=0, row_index=1)
    solvedBoard.set_original(original_value='5', column_index=1, row_index=1)
    solvedBoard.set_original(original_value='6', column_index=2, row_index=1)
    solvedBoard.set_original(original_value='7', column_index=3, row_index=1)
    solvedBoard.set_original(original_value='8', column_index=4, row_index=1)
    solvedBoard.set_original(original_value='9', column_index=5, row_index=1)
    solvedBoard.set_original(original_value='1', column_index=6, row_index=1)
    solvedBoard.set_original(original_value='2', column_index=7, row_index=1)
    solvedBoard.set_original(original_value='3', column_index=8, row_index=1)
    solvedBoard.set_original(original_value='7', column_index=0, row_index=2)
    solvedBoard.set_original(original_value='8', column_index=1, row_index=2)
    solvedBoard.set_original(original_value='9', column_index=2, row_index=2)
    solvedBoard.set_original(original_value='1', column_index=3, row_index=2)
    solvedBoard.set_original(original_value='2', column_index=4, row_index=2)
    solvedBoard.set_original(original_value='3', column_index=5, row_index=2)
    solvedBoard.set_original(original_value='4', column_index=6, row_index=2)
    solvedBoard.set_original(original_value='5', column_index=7, row_index=2)
    solvedBoard.set_original(original_value='6', column_index=8, row_index=2)
    solvedBoard.set_original(original_value='2', column_index=0, row_index=3)
    solvedBoard.set_original(original_value='3', column_index=1, row_index=3)
    solvedBoard.set_original(original_value='4', column_index=2, row_index=3)
    solvedBoard.set_original(original_value='5', column_index=3, row_index=3)
    solvedBoard.set_original(original_value='6', column_index=4, row_index=3)
    solvedBoard.set_original(original_value='7', column_index=5, row_index=3)
    solvedBoard.set_original(original_value='8', column_index=6, row_index=3)
    solvedBoard.set_original(original_value='9', column_index=7, row_index=3)
    solvedBoard.set_original(original_value='1', column_index=8, row_index=3)
    solvedBoard.set_original(original_value='5', column_index=0, row_index=4)
    solvedBoard.set_original(original_value='6', column_index=1, row_index=4)
    solvedBoard.set_original(original_value='7', column_index=2, row_index=4)
    solvedBoard.set_original(original_value='8', column_index=3, row_index=4)
    solvedBoard.set_original(original_value='9', column_index=4, row_index=4)
    solvedBoard.set_original(original_value='1', column_index=5, row_index=4)
    solvedBoard.set_original(original_value='2', column_index=6, row_index=4)
    solvedBoard.set_original(original_value='3', column_index=7, row_index=4)
    solvedBoard.set_original(original_value='4', column_index=8, row_index=4)
    solvedBoard.set_original(original_value='8', column_index=0, row_index=5)
    solvedBoard.set_original(original_value='9', column_index=1, row_index=5)
    solvedBoard.set_original(original_value='1', column_index=2, row_index=5)
    solvedBoard.set_original(original_value='2', column_index=3, row_index=5)
    solvedBoard.set_original(original_value='3', column_index=4, row_index=5)
    solvedBoard.set_original(original_value='4', column_index=5, row_index=5)
    solvedBoard.set_original(original_value='5', column_index=6, row_index=5)
    solvedBoard.set_original(original_value='6', column_index=7, row_index=5)
    solvedBoard.set_original(original_value='7', column_index=8, row_index=5)
    solvedBoard.set_original(original_value='3', column_index=0, row_index=6)
    solvedBoard.set_original(original_value='4', column_index=1, row_index=6)
    solvedBoard.set_original(original_value='5', column_index=2, row_index=6)
    solvedBoard.set_original(original_value='6', column_index=3, row_index=6)
    solvedBoard.set_original(original_value='7', column_index=4, row_index=6)
    solvedBoard.set_original(original_value='8', column_index=5, row_index=6)
    solvedBoard.set_original(original_value='9', column_index=6, row_index=6)
    solvedBoard.set_original(original_value='1', column_index=7, row_index=6)
    solvedBoard.set_original(original_value='2', column_index=8, row_index=6)
    solvedBoard.set_original(original_value='6', column_index=0, row_index=7)
    solvedBoard.set_original(original_value='7', column_index=1, row_index=7)
    solvedBoard.set_original(original_value='8', column_index=2, row_index=7)
    solvedBoard.set_original(original_value='9', column_index=3, row_index=7)
    solvedBoard.set_original(original_value='1', column_index=4, row_index=7)
    solvedBoard.set_original(original_value='2', column_index=5, row_index=7)
    solvedBoard.set_original(original_value='3', column_index=6, row_index=7)
    solvedBoard.set_original(original_value='4', column_index=7, row_index=7)
    solvedBoard.set_original(original_value='5', column_index=8, row_index=7)
    solvedBoard.set_original(original_value='9', column_index=0, row_index=8)
    solvedBoard.set_original(original_value='1', column_index=1, row_index=8)
    solvedBoard.set_original(original_value='2', column_index=2, row_index=8)
    solvedBoard.set_original(original_value='3', column_index=3, row_index=8)
    solvedBoard.set_original(original_value='4', column_index=4, row_index=8)
    solvedBoard.set_original(original_value='5', column_index=5, row_index=8)
    solvedBoard.set_original(original_value='6', column_index=6, row_index=8)
    solvedBoard.set_original(original_value='7', column_index=7, row_index=8)
    solvedBoard.set_original(original_value='8', column_index=8, row_index=8)

    yield solvedBoard

@fixture()
def very_easy_board(solved_board):
    veryEasyBoard = solved_board
    veryEasyBoard.set_original(original_value=' ', column_index=0, row_index=0)
    veryEasyBoard.set_original(original_value=' ', column_index=2, row_index=6)
    veryEasyBoard.set_original(original_value=' ', column_index=3, row_index=0)

    yield veryEasyBoard

def test_solved_board(solved_board):
    solvedBoard = solved_board

    assert(solvedBoard.get_original(column_index=7, row_index=5) == '6')
    assert(solvedBoard.get_original(column_index=6, row_index=3) == '8')

    print(f'Here is the solved Board:\n{solvedBoard}')
    assert(solvedBoard.is_valid())
    assert(solvedBoard.is_solved())

def test_unsolved_board(solved_board):
    solvedBoard = solved_board

    # Make it unsolved
    unsolvedBoard = deepcopy(solvedBoard)
    unsolvedBoard.set_original(original_value=' ', column_index=4, row_index=4)
    unsolvedBoard.set_original(original_value=' ', column_index=5, row_index=4)
    unsolvedBoard.set_original(original_value=' ', column_index=6, row_index=4)
    print(f'Here is the unsolved Board:\n{unsolvedBoard}')

    assert(unsolvedBoard.is_valid())
    assert(not unsolvedBoard.is_solved())

def test_invalid_character(solved_board):
    solvedBoard = solved_board

    # Invalid Character
    invalidBoard = deepcopy(solvedBoard)
    invalidBoard.set_original(original_value='?', column_index=4, row_index=4)
    print(f'Here is the invalid Board with an invalid character:\n{invalidBoard}')

    assert(not invalidBoard.is_valid())
    assert(not invalidBoard.is_solved())

def test_invalid_duplicate_in_row(solved_board):
    solvedBoard = solved_board

    # Duplicate in a Row
    invalidBoard = deepcopy(solvedBoard)
    invalidBoard.set_original(original_value='9', column_index=0, row_index=0)
    invalidBoard.set_original(original_value=' ', column_index=2, row_index=2)
    invalidBoard.set_original(original_value=' ', column_index=0, row_index=8)
    print(f'Here is the invalid Board with an duplicate character in a row:\n{invalidBoard}')

    assert(not invalidBoard.is_valid())
    assert(not invalidBoard.is_solved())

def test_invalid_duplicate_in_column(solved_board):
    solvedBoard = solved_board

    # Duplicate in a Row
    invalidBoard = deepcopy(solvedBoard)
    invalidBoard.set_original(original_value='9', column_index=0, row_index=0)
    invalidBoard.set_original(original_value=' ', column_index=2, row_index=2)
    invalidBoard.set_original(original_value=' ', column_index=8, row_index=0)
    print(f'Here is the invalid Board with an duplicate character in a column:\n{invalidBoard}')

    assert(not invalidBoard.is_valid())
    assert(not invalidBoard.is_solved())

def test_invalid_duplicate_in_box(solved_board):
    solvedBoard = solved_board

    # Duplicate in a Row
    invalidBoard = deepcopy(solvedBoard)
    invalidBoard.set_original(original_value='9', column_index=0, row_index=0)
    invalidBoard.set_original(original_value=' ', column_index=0, row_index=8)
    invalidBoard.set_original(original_value=' ', column_index=8, row_index=0)
    print(f'Here is the invalid Board with an duplicate character in a boxw:\n{invalidBoard}')

    assert(not invalidBoard.is_valid())
    assert(not invalidBoard.is_solved())
def test_equal_boards(solved_board):
    solvedBoard = solved_board
    secondBoard = deepcopy(solvedBoard)

    assert(solvedBoard == secondBoard)

def test_unequal_boards(solved_board):
    solvedBoard = solved_board
    secondBoard = deepcopy(solvedBoard)
    secondBoard.set_original(original_value=' ', column_index=0, row_index=0)

    assert(not solvedBoard == secondBoard)

def test_solve_very_easy_case(very_easy_board):
    veryEasyBoard = very_easy_board
    print(f'Here is the Unsolved Very Easy Board:\n{veryEasyBoard}')
    solveWasSuccessful = veryEasyBoard.solve()
    print(f'Here is the Solved Very Easy Board:\n{veryEasyBoard}')
    assert(solveWasSuccessful)



'''



def testGenerateRandomBoard():)
    print('Test Generate Board.'))
    # Create Empty Board.)
    testEmptyBoard=SudokuBoard())
    print('I have created an empty sudoku board, it looks like this:\n' + str(testEmptyBoard))
)
    # Generate a random board)
    testEmptyBoard.generateBoard())
    print('Generated this board:\n' + str(testEmptyBoard))
)
    # Solve the board. Just find one solution.)
    print('Solving the board, looking for just one solution'))
    testEmptyBoard.solve(recursionDepth=1, findAllPossible=False)
)
    # Print the solved board.)
    if(testEmptyBoard is not None):)
        print('There are ' + str(len(testEmptyBoard.solvedBoardList)) + ' solutions!'))
        #print('Here is the solved board:\n' + str(testEmptyBoard)))
        #print('No actually here is the solved board:\n' + str([0])))
    else:)
        print('I could not solve the board, the method returned a None.')

def testBoards():)
    #testSolvedBoard())
    #testInvalidBoard())
    testIncompleteBoard())
    #testHalfSolvedBoard()

def testSolvedBoard():

def testHalfSolvedBoard():)
    halfSolvedBoard = SudokuBoard())
    halfSolvedBoard.board=[)
     1,2,3,4,5,6,7,8,9)
    ,4,5,6,7,8,9,1,2,3)
    ,7,8,9,1,2,3,4,5,6)
    ,2,3,4,5,6,7,8,9,1)
    ,5,6,7,8,9,1,2,3,4)
    ,0,0,0,0,3,4,5,6,7)
    ,0,0,0,0,0,0,0,0,0)
    ,0,0,0,0,0,0,0,0,0)
    ,0,0,0,0,0,0,0,0,0)
    ]
)
    print('This half board should be valid!:' + str(halfSolvedBoard.isValid())))
    print('This valid&Solved board should NOT be solved:' + str(halfSolvedBoard.isSolved()))
)
    findAllPossible=False)
    print('Solving the half solved board, findAllPossibleSolutions=' + str(findAllPossible))
)
    halfSolvedBoard.solve(recursionDepth=1, findAllPossible=findAllPossible))
    print('I found ' + str(len(halfSolvedBoard.solvedBoardList)) + ' solved boards!'))
    #halfSolvedBoard.removeDuplicateSolvedBoards())
    #for solvedBoard in halfSolvedBoard.solvedBoardList:)
    #    print(str(solvedBoard)))
    print('After removing duplicates, there are ' + str(len(halfSolvedBoard.solvedBoardList)) + ' solved boards!'))
    print('This is the first solved board:\n' + str(halfSolvedBoard.solvedBoardList[0]))

def testInvalidBoard():)
    invalidBoard = SudokuBoard())
    invalidBoard.board=[)
     1,1,3,4,5,6,7,8,9)
    ,4,5,6,7,8,9,1,2,3)
    ,7,8,9,1,2,3,4,5,6)
    ,2,3,4,5,6,7,8,9,1)
    ,5,6,7,8,9,1,2,3,4)
    ,8,9,1,2,3,4,5,6,7)
    ,3,4,5,6,7,8,9,1,2)
    ,6,7,8,9,1,2,3,4,5)
    ,9,1,2,3,4,5,6,7,8)
    ]
)
    print('This invalidBoard board should NOT be valid!:' + str(invalidBoard.isValid())))
    print('This invalidBoard board should NOT be solved:' + str(invalidBoard.isSolved()))
)
    print('Solving the invalid board...'))
    invalidBoard.solve())
    print('The solved boards should be length zero:' + str(invalidBoard.solvedBoardList))

def testIncompleteBoard():)
    incompleteBoard = SudokuBoard())
    incompleteBoard.board=[)
     1,2,3,4,5,6,7,8,0)
    ,4,5,6,7,8,9,1,2,3)
    ,7,8,9,1,2,3,4,5,6)
    ,2,3,4,5,0,7,8,9,1)
    ,5,6,7,8,9,1,2,3,4)
    ,8,9,1,2,3,4,5,6,0)
    ,3,4,5,6,7,8,0,1,2)
    ,6,7,8,9,1,2,3,4,5)
    ,0,1,2,3,4,5,6,0,0)
    ]
)
    print('This incompleteBoard board should be valid!:' + str(incompleteBoard.isValid())))
    print('This incompleteBoard board should NOT be solved:' + str(incompleteBoard.isSolved()))
)
    print('Solving the incomplete board....'))
    incompleteBoard.solve())
    print('The solved boards should be one:' + str(len(incompleteBoard.solvedBoardList)))



'''
