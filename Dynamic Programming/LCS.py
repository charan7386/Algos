def dp_LCS(A, B, n1, n2):
    L = [[0]*(n2+1) for i in range(n1+1)]
    for i in range(n1+1):
        for j in range(n2+1):
            if(i == 0 or j==0):
                L[i][j] = 0
            elif(A[i-1] == B[j-1]):
                L[i][j] = 1+L[i-1][j-1]
            else:
                L[i][j] = max(L[i][j-1], L[i-1][j])
    return L[n1][n2]

def rec_LCS(A, B, i, j, n1, n2):
    if(i == n1 or j==n2):
        return 0
    elif(A[i] == B[j]):
        return 1+rec_LCS(A, B, i+1, j+1, n1, n2)
    else:
        return max(rec_LCS(A, B, i, j+1, n1, n2), rec_LCS(A, B, i+1, j, n1, n2))

A = raw_input()
B = raw_input()
print rec_LCS(A, B, 0, 0, len(A), len(B))
print dp_LCS(A, B, len(A), len(B))
