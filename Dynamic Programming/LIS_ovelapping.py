#Approach: Exclude and Include elements and do like knapsack

import sys

def LIS(A, i, n, prev, cache):
    if(i==n):
        return 0
    key = (i, prev)
    if(key in cache):
        value = cache[key]
    else:
        exclude = LIS(A, i+1, n, prev, cache)
        include = 0
        if(A[i]>prev):
            include = 1+LIS(A, i+1, n, A[i], cache)
        value = max(exclude, include)
        cache[key] = value
    return value

A = map(int, raw_input().split())
cache = {}
print LIS(A, 0, len(A), -sys.maxint-1, cache)
