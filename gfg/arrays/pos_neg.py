def fn(A, n):
    i = -1
    for j in range(n):
        if(A[j]<0):
            i += 1
            A[i], A[j] = A[j], A[i]
    neg = 0
    pos = i+1
    while(neg<pos and pos<n and A[neg]<0):
        A[neg], A[pos] = A[pos], A[neg]
        neg += 2
        pos += 1
    return A


A = list(map(int, input().split()))
A = fn(A, len(A))
print(A)
