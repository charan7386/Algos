def ans(A, n):
    ones = 0
    twos = 0
    for i in range(n):
        twos |= ones & A[i]
        ones ^= A[i]
        common = ~(ones & twos)
        ones &= common
        twos &= common
    return ones

A = map(int, raw_input().split())
print(ans(A, len(A)))
