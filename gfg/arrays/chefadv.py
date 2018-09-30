t = int(input())
while t != 0 :
    n,m,x,y = input().split(" ")
    n = int(n)   
    m = int(m)   
    x = int(x)   
    y = int(y)   

    k = 1
    p = 1

    if n<=0 or m<=0 or x<=0 or y<=0:
            print("Pofik")         
    elif n-k==1 and m-p==1:
        print("Chefirnemo")
    else:
        if (n-k)%x==0 and (m-p)%y==0:
            print("Chefirnemo")
        elif (n-k-1)%x==0 and (m-p-1)%y==0:
            if n-k-1>=0 and m-p-1>=0:
                print("Chefirnemo")
            else:
                print("Pofik")                
        else:
            print("Pofik")
    t-=1