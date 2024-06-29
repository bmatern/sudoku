PROJECT_PATH=/Users/ben/github/sudoku


source activate sudoku
BIN_PATH=`pwd`
cd PROJECT_PATH
python $BIN_PATH"/sudoku_main.py" --task "GENERATE_BOARD"
echo $BIN_PATH
