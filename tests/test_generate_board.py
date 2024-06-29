from pytest import fixture
from copy import deepcopy

from sudoku.board import SudokuBoard

@fixture()
def empty_board():
    emptyBoard = SudokuBoard()

    yield emptyBoard
@fixture()
def solved_board():
    solvedBoard = SudokuBoard()
    solvedBoard.board[0][0].original_value = '1'
    solvedBoard.board[1][0].original_value = '2'
    solvedBoard.board[2][0].original_value = '3'
    solvedBoard.board[3][0].original_value = '4'
    solvedBoard.board[4][0].original_value = '5'
    solvedBoard.board[5][0].original_value = '6'
    solvedBoard.board[6][0].original_value = '7'
    solvedBoard.board[7][0].original_value = '8'
    solvedBoard.board[8][0].original_value = '9'
    solvedBoard.board[0][1].original_value = '4'
    solvedBoard.board[1][1].original_value = '5'
    solvedBoard.board[2][1].original_value = '6'
    solvedBoard.board[3][1].original_value = '7'
    solvedBoard.board[4][1].original_value = '8'
    solvedBoard.board[5][1].original_value = '9'
    solvedBoard.board[6][1].original_value = '1'
    solvedBoard.board[7][1].original_value = '2'
    solvedBoard.board[8][1].original_value = '3'
    solvedBoard.board[0][2].original_value = '7'
    solvedBoard.board[1][2].original_value = '8'
    solvedBoard.board[2][2].original_value = '9'
    solvedBoard.board[3][2].original_value = '1'
    solvedBoard.board[4][2].original_value = '2'
    solvedBoard.board[5][2].original_value = '3'
    solvedBoard.board[6][2].original_value = '4'
    solvedBoard.board[7][2].original_value = '5'
    solvedBoard.board[8][2].original_value = '6'
    solvedBoard.board[0][3].original_value = '2'
    solvedBoard.board[1][3].original_value = '3'
    solvedBoard.board[2][3].original_value = '4'
    solvedBoard.board[3][3].original_value = '5'
    solvedBoard.board[4][3].original_value = '6'
    solvedBoard.board[5][3].original_value = '7'
    solvedBoard.board[6][3].original_value = '8'
    solvedBoard.board[7][3].original_value = '9'
    solvedBoard.board[8][3].original_value = '1'
    solvedBoard.board[0][4].original_value = '5'
    solvedBoard.board[1][4].original_value = '6'
    solvedBoard.board[2][4].original_value = '7'
    solvedBoard.board[3][4].original_value = '8'
    solvedBoard.board[4][4].original_value = '9'
    solvedBoard.board[5][4].original_value = '1'
    solvedBoard.board[6][4].original_value = '2'
    solvedBoard.board[7][4].original_value = '3'
    solvedBoard.board[8][4].original_value = '4'
    solvedBoard.board[0][5].original_value = '8'
    solvedBoard.board[1][5].original_value = '9'
    solvedBoard.board[2][5].original_value = '1'
    solvedBoard.board[3][5].original_value = '2'
    solvedBoard.board[4][5].original_value = '3'
    solvedBoard.board[5][5].original_value = '4'
    solvedBoard.board[6][5].original_value = '5'
    solvedBoard.board[7][5].original_value = '6'
    solvedBoard.board[8][5].original_value = '7'
    solvedBoard.board[0][6].original_value = '3'
    solvedBoard.board[1][6].original_value = '4'
    solvedBoard.board[2][6].original_value = '5'
    solvedBoard.board[3][6].original_value = '6'
    solvedBoard.board[4][6].original_value = '7'
    solvedBoard.board[5][6].original_value = '8'
    solvedBoard.board[6][6].original_value = '9'
    solvedBoard.board[7][6].original_value = '1'
    solvedBoard.board[8][6].original_value = '2'
    solvedBoard.board[0][7].original_value = '6'
    solvedBoard.board[1][7].original_value = '7'
    solvedBoard.board[2][7].original_value = '8'
    solvedBoard.board[3][7].original_value = '9'
    solvedBoard.board[4][7].original_value = '1'
    solvedBoard.board[5][7].original_value = '2'
    solvedBoard.board[6][7].original_value = '3'
    solvedBoard.board[7][7].original_value = '4'
    solvedBoard.board[8][7].original_value = '5'
    solvedBoard.board[0][8].original_value = '9'
    solvedBoard.board[1][8].original_value = '1'
    solvedBoard.board[2][8].original_value = '2'
    solvedBoard.board[3][8].original_value = '3'
    solvedBoard.board[4][8].original_value = '4'
    solvedBoard.board[5][8].original_value = '5'
    solvedBoard.board[6][8].original_value = '6'
    solvedBoard.board[7][8].original_value = '7'
    solvedBoard.board[8][8].original_value = '8'

    yield solvedBoard

@fixture()
def very_easy_board(solved_board):
    veryEasyBoard = solved_board
    veryEasyBoard.board[0][0].original_value = ' '
    veryEasyBoard.board[2][6].original_value = ' '
    veryEasyBoard.board[3][0].original_value = ' '

    yield veryEasyBoard

def test_solved_board(solved_board):
    solvedBoard = solved_board

    assert(solvedBoard.board[7][5].original_value== '6')
    assert(solvedBoard.board[6][3].original_value== '8')

    print(f'Here is the solved Board:\n{solvedBoard}')
    assert(solvedBoard.is_valid())
    assert(solvedBoard.is_solved())

def test_unsolved_board(solved_board):
    solvedBoard = solved_board

    # Make it unsolved
    unsolvedBoard = deepcopy(solvedBoard)
    unsolvedBoard.board[4][4].original_value = ' '
    unsolvedBoard.board[5][4].original_value = ' '
    unsolvedBoard.board[6][4].original_value = ' '
    print(f'Here is the unsolved Board:\n{unsolvedBoard}')

    assert(unsolvedBoard.is_valid())
    assert(not unsolvedBoard.is_solved())

def test_invalid_character(solved_board):
    solvedBoard = solved_board

    # Invalid Character
    invalidBoard = deepcopy(solvedBoard)
    invalidBoard.board[4][4].original_value='?'
    #invalidBoard.set_original(original_value='?', column_index=4, row_index=4)
    print(f'Here is the invalid Board with an invalid character:\n{invalidBoard}')

    assert(not invalidBoard.is_valid())
    assert(not invalidBoard.is_solved())

def test_invalid_duplicate_in_row(solved_board):
    solvedBoard = solved_board

    # Duplicate in a Row
    invalidBoard = deepcopy(solvedBoard)
    invalidBoard.board[0][0].original_value = '9'
    invalidBoard.board[2][2].original_value = ' '
    invalidBoard.board[0][8].original_value = ' '
    print(f'Here is the invalid Board with an duplicate character in a row:\n{invalidBoard}')

    assert(not invalidBoard.is_valid())
    assert(not invalidBoard.is_solved())

def test_invalid_duplicate_in_column(solved_board):
    solvedBoard = solved_board

    # Duplicate in a Row
    invalidBoard = deepcopy(solvedBoard)
    invalidBoard.board[0][0].original_value = '9'
    invalidBoard.board[2][2].original_value = ' '
    invalidBoard.board[8][0].original_value = ' '
    print(f'Here is the invalid Board with an duplicate character in a column:\n{invalidBoard}')

    assert(not invalidBoard.is_valid())
    assert(not invalidBoard.is_solved())

def test_invalid_duplicate_in_box(solved_board):
    solvedBoard = solved_board

    # Duplicate in a Row
    invalidBoard = deepcopy(solvedBoard)
    invalidBoard.board[0][0].original_value = '9'
    invalidBoard.board[0][8].original_value = ' '
    invalidBoard.board[8][0].original_value = ' '
    print(f'Here is the invalid Board with an duplicate character in a box:\n{invalidBoard}')

    assert(not invalidBoard.is_valid())
    assert(not invalidBoard.is_solved())
def test_equal_boards(solved_board):
    solvedBoard = solved_board
    secondBoard = deepcopy(solvedBoard)

    assert(solvedBoard == secondBoard)

def test_unequal_boards(solved_board):
    solvedBoard = solved_board
    secondBoard = deepcopy(solvedBoard)
    secondBoard.board[0][0].original_value = ' '

    assert(not solvedBoard == secondBoard)

def test_solve_very_easy_case(very_easy_board):
    veryEasyBoard = very_easy_board
    print(f'Here is the Unsolved Very Easy Board:\n{veryEasyBoard}')
    solveWasSuccessful = veryEasyBoard.solve()
    print(f'Here is the Solved Very Easy Board:\n{veryEasyBoard}')
    assert(solveWasSuccessful)


def test_solve_empty_board(empty_board):
    emptyBoard = empty_board
    print(f'Here is the Empty Board:\n{emptyBoard}')
    solveWasSuccessful = emptyBoard.solve(printBoard=False)
    print(f'Here is the Solved Empty Board:\n{emptyBoard}')
    assert(solveWasSuccessful)

