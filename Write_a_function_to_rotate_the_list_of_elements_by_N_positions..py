n=int(input())
l=list(map(int,input().split()))
a=int(input())
for a in range(a):
    for i in range(1,n):
        for j in range(n-1):
            l[j],l[j+1]=l[j+1],l[j]
for b in l:
    print(b,end=' ')