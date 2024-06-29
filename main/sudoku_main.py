from sys import exc_info
import argparse

from sudoku.board import SudokuBoard


def parseArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--task", required=False, help="task to perform", type=str)

    return parser.parse_args()


def generate_random_board():
    # TODO Seed randomly

    emptyBoard = SudokuBoard()
    emptyBoard.solve()
    print(f'This is my solved random board:{emptyBoard}')


if __name__=='__main__':
    try:
        args=parseArgs()
        task = args.task

        if(task=='GENERATE_BOARD'):
            generate_random_board()
        else:
            print('No task to perform ')


    except Exception:
        print ('Unexpected problem running sudoku:')
        print (str(exc_info()))
        raise
