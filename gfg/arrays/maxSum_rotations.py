def fn(A, n):
    total = 0
    cur = 0
    for i in range(n):
        total += A[i]
        cur += i*A[i]
    ans = cur
    for i in range(1, n):
        cur = cur + total - n*A[n-i]
        if(cur > ans):
            ans = cur
    return ans

A = list(map(int, input().split()))
print(fn(A, len(A)))
