def search(A, n, key):
    pivot = findPivot(A, 0, n-1)
    if(pivot == -1):
        return binarySearch(A, 0, n-1, key)
    if(A[pivot] == key):
        return pivot
    if(A[0] <= key):
        return binarySearch(A, 0, pivot-1, key)
    return binarySearch(A, pivot+1, n-1, key)

def findPivot(A, low, high):
    if(high < low):
        return -1
    if(high == low):
        return high
    mid = int((low+high)/2)
    if(mid < high and A[mid]>A[mid+1]):
        return mid
    if(mid>low and A[mid-1] > A[mid]):
        return mid-1
    if(A[low]>=A[mid]):
        return findPivot(A, low, mid-1)
    return findPivot(A, mid+1, high)

def binarySearch(arr, low, high, key):
	if high < low:
		return -1
	mid = int((low + high)/2)
	if key == arr[mid]:
		return mid
	if key > arr[mid]:
		return binarySearch(arr, (mid + 1), high, key);
	return binarySearch(arr, low, (mid -1), key);

A = list(map(int, input().split()))
print(search(A, len(A), 3))
