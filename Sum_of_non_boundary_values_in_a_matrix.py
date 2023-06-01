n,m=map(int,input().split())
l=[]
for i in range(n):
    s=list(map(int,input().split()))
    l.append(s)
s1=0
for i in range(n):
    for j in range(m):
        if(i!=0 and i!=n-1 and j!=0 and j!=m-1):
            s1=s1+l[i][j]
print(s1)      
