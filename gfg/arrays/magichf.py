t = int(input())
while t != 0 :
    n,x,s = input().split(" ")
    n = int(n)
    x = int(x)
    s = int(s)
    swaps = []
    for i in range(0,s):
        a,b = input().split(" ")
        swaps.append(int(a))
        swaps.append(int(b))
    i = 0
    j = 1
    for k in range(0,s):
        if x==swaps[i] or x==swaps[j]:
            if x == swaps[i]:
                x = swaps[j]
            else:
                x = swaps[i]
            i+=2
            j+=2
        else:
            i+=2
            j+=2

    print(x)    

    t-=1