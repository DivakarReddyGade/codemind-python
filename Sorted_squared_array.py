n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    a=i*i
    l1.append(a)
l1.sort()
print(*l1)