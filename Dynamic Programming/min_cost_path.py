import sys

def minCost(cost, m, n):
    if(m<0 or n<0):
        return sys.maxint
    elif(m == 0 and n == 0):
        return cost[m][n]
    else:
        return cost[m][n] + min(minCost(cost, m-1, n), minCost(cost, m, n-1), minCost(cost, m-1, n-1))

def dp(cost,m, n):
    L = [[0]*(m+1) for x in range(n+1)]
    L[0][0] = cost[0][0]
    for i in range(1, m+1):
        L[i][0] = L[i-1][0] + cost[i][0]
    for i in range(1, n+1):
        L[0][i] = L[0][i-1] + cost[0][i]
    for i in range(1, m+1):
        for j in range(1, n+1):
            L[i][j] = min(L[i-1][j], L[i][j-1], L[i-1][j-1])+cost[i][j]
    return L[m][n]

cost= [ [1, 2, 3], [4, 8, 2], [1, 5, 3] ]
print minCost(cost, 2, 2)
print dp(cost, 2, 2)
