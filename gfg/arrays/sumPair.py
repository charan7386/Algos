def search(A, n, x):
    for i in range(n):
        if(A[i] > A[i+1]):
            break
    l = (i+1)%n
    r = i
    while(l != r):
        if(A[l]+A[r] == x):
            return True
        if(A[l]+A[r] < x):
            l = (l+1)%n
        else:
            r = (n+r-1)%n
    return False

def searchCount(A, n, x):
    for i in range(n):
        if(A[i] > A[i+1]):
            break
    l = (i+1)%n
    r = i
    cnt = 0
    while(l != r):
        if(A[l]+A[r] == x):
            cnt += 1
            l = (l+1)%n
            r = (n+r-1)%n
        elif(A[l]+A[r] < x):
            l = (l+1)%n
        else:
            r = (n+r-1)%n
    return cnt


A = list(map(int, input().split()))
print(search(A, len(A), 16))
print(searchCount(A, len(A), 16))
