n=int(input())
l=set(map(int,input().split()))
s=sum(l)
for i in range(n,0,-1):
    if(s%i==0):
        m=i
        break
print(m)