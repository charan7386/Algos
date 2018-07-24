def solve(A, start, end, curr_sum, x, req):
    if(start>=end):
        return
    if(curr_sum + A[start] == req):
        x[start] = 1
        for i in range(len(x)):
            if(x[i] == 1):
                print A[i],
        print
        return
    if(curr_sum + A[start] > req):
        return
    x[start] = 1
    solve(A, start+1, end, curr_sum-A[start], x, req)
    x[start] = 0
    solve(A, start+1, end, curr_sum, x, req)

A = map(int, raw_input().split())
req = int(raw_input())
solve(A, 0, len(A)-1, 0, [0 for x in range(len(A))], req)
