def count(A, m, n):
    if(n == 0):
        return 1
    if(n < 0):
        return 0
    if(m<=0 and n>=1):
        return 0
    return count(A, m-1, n) + count(A, m, n-A[m-1])

A = map(int, raw_input().split())
value = int(raw_input())
print count(A, len(A), value)
