def swapBits(A, p1, p2, n):
    set1 = (A>>p1) & ((1<<n)-1)
    set2 = (A>>p2) & ((1<<n)-1)
    xor = set1^set2
    xor = (xor<<p1) | (xor<<p2)
    return xor^A

A = int(raw_input())
p1, p2, n = map(int, raw_input().split())
print swapBits(A, p1, p2, n)
