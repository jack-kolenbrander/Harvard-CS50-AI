"""
Tic Tac Toe Player
"""

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
    x_count = 0
    o_count = 0
    empty_count = 0
    for row in board:
        for cell in row:
            if board[row][cell] == X:
                x_count += 1
            elif board[row][cell] == O:
                o_count += 1
            else:
                empty_count += 1
    
    if empty_count == 9:
        return X
    elif x_count + o_count == 9:
        return X
    elif x_count > o_count:
        return O
    elif x_count == o_count:
        return X

    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    for row in board:
        for cell in row:
            if board[row][cell] == EMPTY:
                actions.add((row,cell))
    
    return actions

    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # create copy of board
    new_board = copy.deepcopy(board)
    #check who's turn it is
    turn = player(new_board)
    # return copy of board after making an action
    new_board[action[0]][action[1]] = turn

    return new_board
            
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    #check diagonals

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]
    
    #check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != EMPTY:
            return row[0]
    
    #check columns
    if board[0][0] == board[1][0] == board [2][0] and board [0][0] != EMPTY:
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1] and board [0][1] != EMPTY:
        return board[0][1]
    elif board[0][2] == board[1][2] == board[2][2] and board [0][2] != EMPTY:
        return board[0][2]
    
    return None
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    empty_count = 0
    for row in board:
        for cell in row:
            if board[row][cell] == EMPTY:
                empty_count += 1
    if winner(board) != None:
        return True
    elif empty_count == 0:
        return True
    else:
        return False
    
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0
    raise NotImplementedError

def max_value(board):
    # set v to negative infinity
    v = float('-inf')
    # if state is terminal return utility
    if terminal(board):
        return utility(board)
    # loop through actions and find maximum value of v
    for action in actions(board):
        v = max(v,min_value(result(board,action)))
    # return v
    return(v)


def min_value(board):
    # set v to infinity
    v = float('inf')
    # check if board is terminal, if so return utility of that board
    if terminal(board):
        return utility(board)
    # loop through actions and find minimum v value
    for action in actions(board):
        v = min(v,max_value(result(board,action)))
    # return v
    return v



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    #if x is player, want to maximize the score
    #if o is player, want to minimize score

    #get player
    current_player = player(board)
    #get possible actions
    current_actions = actions(board)

    if not terminal(board):
        if current_player == X:
            #get current actions
            x_actions = actions(board)\
            # set variables for max score and max action
            max_score = ('-inf')
            max_action = None
            # loop throug actions with min value function
            for action in x_actions:
                score = min_value(result(board,action))
                #if a new max score is found, update
                if score > max_score:
                    max_score = score
                    max_action = action
            #return best action
            return max_action
        elif current_player == O:
            #get current actions
            x_actions = actions(board)\
            # set variables for max score and max action
            min_score = ('inf')
            min_action = None
            # loop throug actions with min value function
            for action in x_actions:
                score = max_value(result(board,action))
                #if a new max score is found, update
                if score < min_score:
                    min_score = score
                    min_action = action
            #return best action
            return min_action
    else:
        return None


    raise NotImplementedError
