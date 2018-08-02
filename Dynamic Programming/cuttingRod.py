import time
start_time = time.time()
import sys

def ans(n, prices, cache, hit):
    if(n <= 0):
        return 0
    key = n
    if(key in cache):
        value = cache[key]
        hit += 1
    else:
        value = -sys.maxint
        for i in range(n):
            value = max(value, prices[i] + ans(n-i-1, prices, cache, hit))
        cache[key] = value
    return value

INT_MIN = -32767

def dp(n, price):
    val = [0 for x in range(n+1)]
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val
    return val[n]


prices = map(int, raw_input().split())
hit = 0
start_time = time.time()
print ans(len(prices), prices, {}, hit)
print time.time() - start_time
start_time = time.time()
print dp(len(prices), prices)
print time.time() - start_time
