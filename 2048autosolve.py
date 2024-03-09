import numpy as np

POSSIBLE_MOVES_COUNT = 4
CELL_COUNT = 4
NUMBER_SQUARES = CELL_COUNT*CELL_COUNT

def initialize_game():
    board = np.zeros((NUMBER_SQUARES), dtype = "int")
    inital_twos = np.random.default_rng().choice(NUMBER_SQUARES,2,replace = False)
    board[inital_twos] = 2
    board = board.reshape((CELL_COUNT,CELL_COUNT))
    return board

def merge(board):
    score = 0
    done = False
    for row in range(CELL_COUNT):
        for col in range(CELL_COUNT):
            if board[row][col] == board[row][col-1] and board[row][col] != 0:
                board[row][col] *=2
                score +=board[row][col]
                board[row][col-1] = 0
                done = True
    return (board, done, score)







def push_board_right(board):
    new = np.zeros((CELL_COUNT,CELL_COUNT), dtype = 'int')
    done = False
    for row in range(CELL_COUNT):
        count = CELL_COUNT - 1
        for col in range(CELL_COUNT -1,-1,-1):
            if board[row][col] != 0:
                new[row][count] = board[row][col]
                if col!=count:
                    done = True
                count -= 1
    return (new,done)



