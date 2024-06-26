from sys import exc_info
import argparse
from os.path import split

from board import SudokuBoard


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





if __name__=='__main__':
    try:
        args=parseArgs()
        task = args.task

        if(task=='GENERATE_BOARD'):

            testBoards()
            #testGenerateRandomBoard()
        else:
            print('No task to perform ')


    except Exception:
        print ('Unexpected problem running sudoku:')
        print (str(exc_info()))
        raise
