def fn(A, n):
    for i in range(n):
        if(A[i] != i and A[i] != -1):
            x = A[i]
            while(A[x] != x and A[x] != -1):
                y = A[x]
                A[x] = x
                x = y
            A[x] = x
            if(A[i] != i):
                A[i] = -1
    return A

def fn_no_neg_one(A, n):
    for i in range(n):
        if(A[i] != i):
            x = A[i]
            while(A[x] != x):
                y = A[x]
                A[x] = x
                x = y
    return B

A = list(map(int, input().split(', ')))
print(fn(A, len(A)))
B = list(map(int, input().split()))
print(fn_no_neg_one(B, len(B)))
