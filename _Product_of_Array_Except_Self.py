n=int(input())
l=list(map(int,input().split()))
for i in range(0,n):
    p=1
    for j in range(0,n):
        if i!=j:
            p*=l[j]
    print(p,end=" ")