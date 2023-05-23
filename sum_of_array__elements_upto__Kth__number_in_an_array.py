n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=0
for i in range(n):
    s=s+l[i]
    if l[i]==k:
        break
print(s)