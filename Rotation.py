s=int(input())
for i in range(s):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    l1=list(tuple(l))
    for k in range(m):
        for i in range(1,len(l1)):
            for j in range(len(l1)-1):
                l[j],l[j+1]=l[j+1],l[j]
    for i in range(len(l)):
        if(i==len(l)-1):
            print(l[i])
        else:
            print(l[i],end=' ')
