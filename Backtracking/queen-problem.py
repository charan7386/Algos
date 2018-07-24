def isSafe(board, row, col):
    for i in range(col):
        if(board[row][i] == 1):
            return False

    for i,j in zip(range(row,-1,-1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False

    for i,j in zip(range(row,4,1), range(col,-1,-1)):
        if board[i][j] == 1:
            return False
    return True

def solve(board, col):
    if(col >= 4):
        return True
    for i in range(4):
        if(isSafe(board, i, col)):
            board[i][col] = 1
            if(solve(board, col+1)):
                return True
            board[i][col] = 0
    return False

def print_sol(sol):
    for i in range(len(sol)):
        print sol[i]

def solveNQ():
    board = []
    for i in range(4):
        board.append([0 for x in range(4)])
    if(solve(board, 0)):
        print_sol(board)
    else:
        print 'Impossible'

solveNQ()
