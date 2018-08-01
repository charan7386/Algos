import functools
import sys
def memoize(f):
	cache = {}
	@functools.wraps(f)
	def newfunc(*args):
		args = tuple(args)
		if args not in cache:
			cache[args] = f(*args)
		return cache[args]
	return newfunc

@memoize
def fn(eggs, floors):
    if(eggs == 1):
        return floors
    if(floors == 0):
        return 0
    ans = sys.maxint
    for i in range(1, floors+1):
        val = max( fn(eggs-1, i-1), fn(eggs, floors-i) ) + 1
        if(ans > val):
            ans = val
    return ans

def drops(eggs, floors, cache):
	if(floors <= 1):
		return floors
	if(eggs == 1):
		return floors
	key = (eggs, floors)
	if key in cache:
		value = cache[key]
	else:
		value = min(1 + max(drops(eggs - 1, floor - 1, cache),
                                drops(eggs, floors - floor, cache))
                        for floor in range(2, floors + 1))
        cache[key] = value
	return value

if __name__ == '__main__':
    n, k = map(int, raw_input().split())
    print fn(n, k)
    print drops(n, k, {})
