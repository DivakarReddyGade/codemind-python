n=int(input())
l=list(map(int,input().split()))
n1=int(input())
l1=list(map(int,input().split()))
l2=[]
for i in range(n):
    l2.append(-1)
for i in range(n):
    l2.insert(l1[i],l[i])
for i in range(n):
    print(l2[i],end=' ')