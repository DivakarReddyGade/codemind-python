a,b=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=[]
for i in l:
    if i in l1 and i not in l2:
        l2.append(i)
print(*l2)
