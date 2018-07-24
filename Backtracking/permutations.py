def permutations(A, l, r):
    if(l == r):
        print ''.join(A)
        return
    for i in range(l, r):
        A[l], A[i] = A[i], A[l]
        permutations(A, l+1, r)
        A[l], A[i] = A[i], A[l]

A = raw_input()
permutations(list(A), 0, len(A))
