n=int(input())
l=list(map(int,input().split()))
s=set(l)
l1=[]
for i in s:
    if i!=max(s):
        l1.append(i)
print(max(l1))