def ans(S, i, j, cache):
    if(i == j):
        return 1
    if(S[i] == S[j] and i+1==j):
        return 2
    key = (i, j)
    if(key in cache):
        value = cache[key]
    else:
        if(S[i] == S[j]):
            value = 2 + ans(S, i+1, j-1, cache)
        else:
            value = max(ans(S, i+1, j, cache), ans(S, i, j-1, cache))
        cache[key] = value
    return value

S = raw_input()
print ans(S, 0, len(S)-1, {})
