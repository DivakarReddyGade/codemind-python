n,m=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(n)]
s=0
s=sum([sum(j) for j in mat])
print(s)