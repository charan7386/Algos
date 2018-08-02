def partitions(A, n, sum, cache):
    if sum == 0:
        return True
    if n == 0 and sum!= 0:
        return False
    key = (n, sum)
    if key in cache:
        ans = cache[key]
    else:
        if(A[n-1]>sum):
            ans = partitions(A, n-1, sum, cache)
        else:
            ans = partitions(A, n-1, sum, cache) or partitions(A, n-1, sum-A[n-1], cache)
        cache[key] = ans
    return ans

A = map(int, raw_input().split())
if(sum(A)%2 == 1):
    print 'Not Possible'
else:
    print partitions(A, len(A), sum(A)/2, {})
