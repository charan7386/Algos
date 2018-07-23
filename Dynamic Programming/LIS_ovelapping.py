#Approach: Exclude and Include elements and do like knapsack

import sys

def LIS(A, i, n, prev):
    if(i==n):
        return 0;
    exclude = LIS(A, i+1, n, prev)
    include = 0
    if(A[i]>prev):
        include = 1+LIS(A, i+1, n, A[i])
    return max(exclude, include)

A = map(int, raw_input().split())
print LIS(A, 0, len(A), -sys.maxint-1)
