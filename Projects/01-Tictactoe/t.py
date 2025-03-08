import math
import copy

X = "X"
O = "O"
EMPTY = None


board = [[EMPTY, O, X],
        [EMPTY, O, X],
        [X, X, O]]

action = (0,0)

#board = [[EMPTY, EMPTY, EMPTY],
#        [EMPTY, EMPTY, EMPTY],
#        [EMPTY, EMPTY, EMPTY]]

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board[action[0]][action[1]] = player(board)
    return board

def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in range(len(board)):
        for j in range(max(len(a) for a in board)):
            if board[i][j] == X:
                count+=1
            elif board[i][j] == O:
                count-=1
    if count:
        return O
    return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(len(board)):
        for j in range(max(len(a) for a in board)):
            if board[i][j] == EMPTY:
                possibleAction = (i,j)
                actions.append(possibleAction)
    return(actions)


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action in actions(board):
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(new_board)
        return new_board
    else:
        raise Exception("accion invalida")
    #missing deep copy instructions


board = [[EMPTY, O, X],
        [EMPTY, O, X],
        [X, X, O]]

print(action)
print(result(board,action))
print(board)

action = (1,0)

print(action)
print(result(board,action))
print(board)