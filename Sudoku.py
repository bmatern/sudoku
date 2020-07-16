from sys import exc_info
import argparse
from os.path import split

from SudokuBoard import SudokuBoard


def parseArgs():
    parser = argparse.ArgumentParser()
    '''
    parser.add_argument("-v", "--validator", required=True, help="validator type", type=str)
    parser.add_argument("-ex", "--excel", required=False, help="input excel file", type=str)
    parser.add_argument("-up", "--upload", required=False, help="upload file name", type=str)
    parser.add_argument("-b", "--bucket", required=False, help="S3 Bucket Name", type=str )
    '''
    parser.add_argument("-t", "--task", required=False, help="task to perform", type=str)

    return parser.parse_args()



def testGenerateRandomBoard():
    print('Test Generate Board.')
    # Create Empty Board.
    testEmptyBoard=SudokuBoard()
    print('I have created an empty sudoku board, it looks like this:\n' + str(testEmptyBoard))

    # Solve the board. Just find one solution.
    print('Solving the board, looking for just one solution')
    testEmptyBoard.solve(recursionDepth=1, findAllPossible=False)

    # Print the solved board.
    if(testEmptyBoard is not None):
        print('Here is the solved board:\n' + str(testEmptyBoard))
    else:
        print('I could not solve the board, the method returned a None.')

def testBoards():
    testSolvedBoard()
    testInvalidBoard()
    testIncompleteBoard()
    testHalfSolvedBoard()

def testSolvedBoard():
    solvedBoard = SudokuBoard()
    solvedBoard.board=[
     1,2,3,4,5,6,7,8,9
    ,4,5,6,7,8,9,1,2,3
    ,7,8,9,1,2,3,4,5,6
    ,2,3,4,5,6,7,8,9,1
    ,5,6,7,8,9,1,2,3,4
    ,8,9,1,2,3,4,5,6,7
    ,3,4,5,6,7,8,9,1,2
    ,6,7,8,9,1,2,3,4,5
    ,9,1,2,3,4,5,6,7,8
    ]
    print('This valid&Solved board should be valid!:' + str(solvedBoard.isValid()))
    print('This valid&Solved board should be solved:' + str(solvedBoard.isSolved()))

def testHalfSolvedBoard():
    halfSolvedBoard = SudokuBoard()
    halfSolvedBoard.board=[
     1,2,3,4,5,6,7,8,9
    ,4,5,6,7,8,9,1,2,3
    ,7,8,9,1,2,3,4,5,6
    ,2,3,4,5,6,7,8,9,1
    ,5,6,7,8,9,1,2,3,4
    ,8,9,1,2,3,4,5,6,7
    ,0,0,0,0,0,0,0,1,2
    ,0,0,0,0,0,0,0,0,0
    ,0,0,0,0,0,0,0,0,0

    ]
    print('This half board should be valid!:' + str(halfSolvedBoard.isValid()))
    print('This valid&Solved board should NOT be solved:' + str(halfSolvedBoard.isSolved()))

    findAllPossible=True
    print('Solving the half solved board, findAllPossibleSolutions=' + str(findAllPossible))

    halfSolvedBoard.solve(recursionDepth=1, findAllPossible=findAllPossible)
    print('I found ' + str(len(halfSolvedBoard.solvedBoardList)) + ' solved boards!')
    halfSolvedBoard.removeDuplicateSolvedBoards()
    #for solvedBoard in halfSolvedBoard.solvedBoardList:
    #    print(str(solvedBoard))
    print('After removing duplicates, there are ' + str(len(halfSolvedBoard.solvedBoardList)) + ' solved boards!')


def testInvalidBoard():
    invalidBoard = SudokuBoard()
    invalidBoard.board=[
     1,1,3,4,5,6,7,8,9
    ,4,5,6,7,8,9,1,2,3
    ,7,8,9,1,2,3,4,5,6
    ,2,3,4,5,6,7,8,9,1
    ,5,6,7,8,9,1,2,3,4
    ,8,9,1,2,3,4,5,6,7
    ,3,4,5,6,7,8,9,1,2
    ,6,7,8,9,1,2,3,4,5
    ,9,1,2,3,4,5,6,7,8
    ]

    print('This invalidBoard board should NOT be valid!:' + str(invalidBoard.isValid()))
    print('This invalidBoard board should NOT be solved:' + str(invalidBoard.isSolved()))

    print('Solving the invalid board...')
    invalidBoard.solve(recursionDepth=1)
    print('The solved boards should be length zero:' + str(invalidBoard.solvedBoardList))

def testIncompleteBoard():
    incompleteBoard = SudokuBoard()
    incompleteBoard.board=[
     1,2,3,4,5,6,7,8,9
    ,4,5,6,7,8,9,1,2,3
    ,7,8,9,1,2,3,4,5,6
    ,2,3,4,5,0,7,8,9,1
    ,5,6,7,8,9,1,2,3,4
    ,8,9,1,2,3,4,5,6,7
    ,3,4,5,6,7,8,9,1,2
    ,6,7,8,9,1,2,3,4,5
    ,9,1,2,3,4,5,6,7,0
    ]

    print('This incompleteBoard board should be valid!:' + str(incompleteBoard.isValid()))
    print('This incompleteBoard board should NOT be solved:' + str(incompleteBoard.isSolved()))

    print('Solving the incomplete board....')
    incompleteBoard.solve(recursionDepth=1)
    print('The solved boards should be one:' + str(len(incompleteBoard.solvedBoardList)))





if __name__=='__main__':
    try:
        args=parseArgs()
        task = args.task

        if(task=='GENERATE_BOARD'):

            #testBoards()
            testGenerateRandomBoard()
        else:
            print('No task to perform ')


    except Exception:
        print ('Unexpected problem running sudoku:')
        print (str(exc_info()))
        raise
