n=int(input())
l=list(map(int,input().split()))
a=l[n-1:n//2-1:-1] 
b=(l[:n//2:1])
for i in a:
    print(i,end=' ')
for i in b:
    print(i,end=' ')
