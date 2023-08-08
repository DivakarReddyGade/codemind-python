t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=list(set(a+b))
    c.sort()
    if (len(c)==n):
        print("YES")
    else:
        print("NO")