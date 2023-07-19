n=int(input())
l=list(map(int,input().split()))
n1=int(input())
l1=list(map(int,input().split()))
m=int(input())
c=0
for i in range(n):
    if(l[i]<=m and l1[i]>=m):
        c+=1
print(c)