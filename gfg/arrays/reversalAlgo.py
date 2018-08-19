
def rotateArray(A, n, d):
	A[:d] = reversed(A[:d])
	A[d:] = reversed(A[d:])
	A = list(reversed(A))
	return A

A = list(map(int, input().split()))
A = rotateArray(A, len(A), 3)
print(A)