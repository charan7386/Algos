def gcd(a, b):
	if(b == 0):
		return a
	return gcd(b, a%b)

def left(A, d, n):
	for i in range(gcd(n, d)):
		j = i
		temp = A[i]
		while True:
			k = j+d
			if(k >= n):
				k = k - n
			if(k == i):
				break
			A[j] = A[k]
			j = k
		A[j] = temp
	return A

def right(A, d, n):
	for i in range(gcd(n, d)):
		j = i
		temp = A[i]
		while True:
			k = j+d
			if(k >= n):
				k = k - n
			if(k == i):
				A[k] = temp
				break
			dummy = A[k]
			A[k] = temp
			temp = dummy
			j = k
	return A

if __name__ == '__main__':
	A = list(map(int, input().split()))
	d = 3
	A = left(A, d, len(A))
	print(A)
	A = right(A, d, len(A))
	print(A)