def LIS(A):
    L = [1]*len(A)
    for i in range(1, len(A)):
        for j in range(i):
            if(A[i]>A[j] and L[i]<L[j]+1):
                L[i] = L[j]+1
    return max(L)

A = map(int, raw_input().split())
print LIS(A)
