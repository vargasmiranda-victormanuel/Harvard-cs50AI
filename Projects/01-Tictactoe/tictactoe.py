"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


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
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    """
    Return any of the variables definned at the begining
    X = "X"
    O = "O"
    EMPTY = None
    """
    transposedBoard = list(map(list,(zip(*board))))
    diagonalBoard = [[board[0][0],board[1][1],board[2][2]],[board[0][2],board[1][1],board[2][0]]]
    joinnedBoard = board + transposedBoard + diagonalBoard
    return(next(iter(checkWinner(joinnedBoard))))

def checkWinner(board):
    for row in board:
        if len(set(row)) == 1 and set(row) != {None}:
            return(set(row))

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    transposedBoard = list(map(list,(zip(*board))))
    diagonalBoard = [[board[0][0],board[1][1],board[2][2]],[board[0][2],board[1][1],board[2][0]]]
    joinnedBoard = board + transposedBoard + diagonalBoard
    
    someoneWone = checkTerminal(joinnedBoard)

    if someoneWone:
        return someoneWone
    else:
        for i in range(len(board)):
            for j in range(max(len(a) for a in board)):
                if board[i][j] == EMPTY:
                    return False
        return(True)

def checkTerminal(board):
    for row in board:
        if len(set(row)) == 1 and set(row) != {None}:
            return(True)
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
