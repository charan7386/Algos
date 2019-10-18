def fn(A, n):
    i = -1
    for j in range(n):
        if(A[j] < 0):
            i += 1
            A[i], A[j] = A[j], A[i]
    return A

#Enter your inputs here
A = list(map(int, input().split(', ')))
print(fn(A, len(A)))
