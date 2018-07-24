def partitions(A, n, sum):
    if sum == 0:
        return True
    if n == 0 and sum!= 0:
        return False
    if(A[n-1]>sum):
        return partitions(A, n-1, sum)
    return partitions(A, n-1, sum) or partitions(A, n-1, sum-A[n-1])

A = map(int, raw_input().split())
if(sum(A)%2 == 1):
    print 'Not Possible'
else:
    print partitions(A, len(A), sum(A)/2)
