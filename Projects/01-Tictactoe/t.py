import math

X = "X"
O = "O"
EMPTY = None


board = [[X, O, X],
        [O, O, X],
        [X, X, O]]

#board = [[EMPTY, EMPTY, EMPTY],
#        [EMPTY, EMPTY, EMPTY],
#        [EMPTY, EMPTY, EMPTY]]

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


print(terminal(board))