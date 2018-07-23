def knapSack(weight, val, wt, n):
    if(n == 0 or weight == 0):
        return 0
    if(wt[n-1]>weight):
        return knapSack(weight, val, wt, n-1)
    return max(val[n-1]+knapSack(weight-wt[n-1], val, wt, n-1), knapSack(weight, val, wt, n-1))

def dp(W, wt, val, n):
    K = [[0 for x in range(W+1)] for x in range(n+1)]
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]],  K[i-1][w])
            else:
                K[i][w] = K[i-1][w]
    return K[n][W]

val = map(int, raw_input().split())
wt = map(int, raw_input().split())
weight = int(raw_input())
print dp(weight, wt, val, len(val))
print knapSack(weight, val, wt, len(val))
