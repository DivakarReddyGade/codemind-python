n=int(input())
l=list(map(int,input().split()))
k=int(input())
s=set(l)
for i in range(k-1):
    s.remove(max(s))
print(max(s))