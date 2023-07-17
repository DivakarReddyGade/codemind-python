n,m=map(int,input().split())
l=list(map(int,input().split()))
l1=list(map(int,input().split()))
l2=[]
l3=[]
for i in l:
    if i not in l1:
        l2.append(i)
for j in l1:
    if j not in l:
        l3.append(j)
l4=l2+l3
for k in l4:
    print(k,end=" ")
