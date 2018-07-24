def editDistance(s1, s2, m, n):
    if(m == 0):
        return n
    if(n == 0):
        return m
    if(s1[m-1] == s2[n-1]):
        return editDistance(s1, s2, m-1, n-1)
    return 1 + min(editDistance(s1, s2, m, n-1), editDistance(s1, s2, m-1, n), editDistance(s1, s2, m-1, n-1))

def dp(s1, s2, m, n):
    L = [[0]*(n+1) for i in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):
            if(i == 0):
                L[i][j] = j
            elif(j == 0):
                L[i][j] = i
            elif(s1[i-1] == s2[j-1]):
                L[i][j] = L[i-1][j-1]
            else:
                L[i][j] = 1 + min(L[i-1][j], L[i][j-1], L[i-1][j-1])
    return L[m][n]

s1 = raw_input()
s2 = raw_input()
print editDistance(s1, s2, len(s1), len(s2))
print dp(s1, s2, len(s1), len(s2))
