# rotates the array to right by once from index 'outOfPlace to cur'
def rightRotate(A, n, outOfPlace, cur):
    temp = A[cur]
    for i in range(cur, outOfPlace, -1):
        A[i] = A[i-1]
    A[outOfPlace] = temp
    return A

def fn(A, n):
    outOfPlace = -1
    for index in range(n):
        if(outOfPlace >= 0):
            # if element at outOfPlace place in negative and if element at index is positive we can rotate the array to right
            # or
            # if element at outOfPlace place in positive and if element at index is negative we can rotate the array to right
            if( (A[index]>=0 and A[outOfPlace]<0) or ( A[index]<0 and A[outOfPlace]>=0 ) ):
                A = rightRotate(A, n, outOfPlace, index)
                if(index-outOfPlace > 2):
                    outOfPlace += 2
                else:
                    outOfPlace=-1
        if(outOfPlace == -1):
            #conditions for A[index] to be in out of place
            if( (A[index]>=0 and index%2==0) or (A[index]<0 and index%2==1) ):
                outOfPlace = index
    return A

A = map(int, raw_input().split())
print(fn(A, len(A)))
