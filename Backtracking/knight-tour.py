#Knight Tour Problem
def isSafe(next_x, next_y, sol, N):
    if(next_x >= 0 and next_x <N and next_y >= 0 and next_y < N and sol[next_x][next_y] == -1):
        return True
    return False

def solveKT(sol, xMove, yMove, x, y, movei, N):
    if(movei == N*N):
        return True
    for k in range(8):
        next_x = x + xMove[k]
        next_y = y + yMove[k]
        if(isSafe(next_x, next_y, sol, N)):
            sol[next_x][next_y] = movei
            if(solveKT(sol, xMove, yMove, next_x, next_y, movei+1, N)):
                return True
            else:
                sol[next_x][next_y] = -1
    return False

def print_sol(sol):
    for i in range(len(sol)):
        print sol[i]

def kt():
    sol = []
    for i in range(8):
        sol.append([-1 for x in range(8)])
    xMove = [2, 1, -1, -2, -2, -1,  1,  2]
    yMove = [1, 2,  2,  1, -1, -2, -2, -1]
    sol[0][0] = 0
    if(solveKT(sol, xMove, yMove, 0, 0, 1, 8)):
        print_sol(sol)
    else:
        print 'Not Possible'

kt()
