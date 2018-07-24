import sys

def matrixOrder(A, i, j):
    if(i == j):
        return 0
    min = sys.maxint
    for k in range(i, j):
        count = matrixOrder(A, i, k) + matrixOrder(A, k+1, j) + A[i-1]*A[k]*A[j]
    if(count <= min):
        min = count
    return min

def matrixOrderDP(p, n):
    m = [[0]*n for x in range(n)]
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1
            m[i][j] = sys.maxint
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j]
                if q < m[i][j]:
                    m[i][j] = q
    return m[1][n-1]

A = map(int, raw_input().split())
print matrixOrder(A, 1, len(A)-1)
print matrixOrderDP(A, len(A))
