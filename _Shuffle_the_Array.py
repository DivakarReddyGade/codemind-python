n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in range(m):
    print(l[i],l[m+i],end=' ')