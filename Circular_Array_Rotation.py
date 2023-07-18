a,b,c=map(int,input().split())
l=list(map(int,input().split()))
for i in range(b):
    for k in range(1,len(l)):
        for j in range(len(l)-1):
            l[j],l[j+1]=l[j+1],l[j]
for i in range(c):
    m=int(input())
    print(l[m])
