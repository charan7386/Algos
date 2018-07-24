def isSafe(maze, m, n, x, y):
    if(x>=0 and x<m and y>=0 and y<n and maze[x][y] == 1):
        return True
    return False

def solveMaze(sol, maze, m, n, x, y):
    if(x==m-1 and y==n-1):
        sol[x][y] = 1
        return True
    if(isSafe(maze, m, n, x, y)):
        sol[x][y] = 1
        if(solveMaze(sol, maze, m, n, x+1, y)):
            return True
        if(solveMaze(sol, maze, m, n, x, y+1)):
            return True
        sol[x][y] = -1
        return False

def print_sol(sol):
    for i in range(len(sol)):
        print sol[i]

def solve(maze, m, n):
    sol = []
    for i in range(m):
        sol.append(['x' for x in range(n)])
    if(solveMaze(sol, maze, m, n, 0, 0)):
        print_sol(sol)
    else:
        print 'Impossible'

m, n = map(int, raw_input().split())
A = []
for i in range(m):
    temp = map(int, raw_input().split())
    A.append(temp)

solve(A, m, n)
