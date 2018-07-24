def coefficient(n, k):
    if(k == 0 or k == n):
        return 1
    return coefficient(n-1, k) + coefficient(n-1, k-1)

def coefficientDP(n, k):
    C = [[0]*(k+1) for x in range(n)]
    for i in range(n+1):
        for j in range(min(i, k)+1):
            if(j == 0 or j == i):
                C[i][j] = 1
            else:
                C[i][j] = C[i-1][j] + C[i-1][j-1]
    return C[n][k]

n, k = map(int, raw_input().split())
print coefficient(n, k)
