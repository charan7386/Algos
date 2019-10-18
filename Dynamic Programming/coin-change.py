def count(A, m, n):
    if(n == 0):
        return 1
    if(n < 0):
        return 0
    if(m<=0 and n>=1):
        return 0
    return count(A, m-1, n) + count(A, m, n-A[m-1])

def countDP(A, m, n, dp):
    if(n == 0):
        return 1
    if(n<0):
        return 0
    if(m<0 and n>=1):
        return 0
    if(dp[m][n] != -1):
        return dp[m][n]
    dp[m][n] = countDP(A, m-1, n, dp) + countDP(A, m, n-A[m], dp)
    return dp[m][n]

#Enter the array here
A = map(int, raw_input().split())
value = int(raw_input())
print count(A, len(A), value)
dp = [[-1]*(value+1) for i in range(len(A)+1)]
print countDP(A, len(A)-1, value, dp)
