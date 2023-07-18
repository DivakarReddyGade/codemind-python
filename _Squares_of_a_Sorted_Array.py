n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    s=i*i
    l1.append(s)
l2=sorted(l1)
for j in l2:
    print(j,end=" ")