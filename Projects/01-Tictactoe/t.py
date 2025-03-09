import math
import copy

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
    winner = checkWinner(joinnedBoard)
    if winner == None:
        return winner
    else:
        return(next(iter(winner)))


def checkWinner(board):
    for row in board:
        if len(set(row)) == 1 and set(row) != {None}:
            return(set(row))
    return None


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
        return True


def checkTerminal(board):
    for row in board:
        if len(set(row)) == 1 and set(row) != {None}:
            return True
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        win = winner(board)
        if win == X:
            return 1
        elif win == O:
            return -1
        elif win == None:
            return 0
    else:
        raise Exception("Utility should be called only if there is a terminal board")


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        return (maxValue(boardInitial)[1])
    elif player(board) == O:
        return (minValue(boardInitial)[1])


def maxValue(board):
    if terminal(board):
        return utility(board), ()
    else:
        value = -100
        bestAction = ()
        for action in actions(board):
            newValue = max(value,minValue(result(board,action))[0])
            if newValue > value:
                bestAction = action
            value = newValue
        return value, bestAction


def minValue(board):
    if terminal(board):
        return utility(board), ()
    else:
        value = 100
        bestAction = ()
        for action in actions(board):
            newValue = min(value,maxValue(result(board,action))[0])
            if newValue < value:
                bestAction = action
            value = newValue
        return value, bestAction

boardInitial = [['X', 'O', None], [None, 'X', 'X'], [None, None, 'O']]

print(minimax(boardInitial))