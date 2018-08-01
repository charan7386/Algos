def fn(A, n, total, cache):
    if(total == 0):
        return True
    if(n == 0 and total != 0):
        return False
    key = (n, total)
    if(key in cache):
        ans = cache[key]
    else:
        if(A[n-1] > total):
            ans = fn(A, n-1, total, cache)
            cache[key] = ans
        else:
            ans = fn(A, n-1, total, cache) or fn(A, n-1, total-A[n-1], cache)
            cache[key] = ans
    return ans

A = map(int, raw_input().split())
total = int(raw_input())
print fn(A, len(A), total, {})
