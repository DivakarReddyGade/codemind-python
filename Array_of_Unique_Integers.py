n=int(input())
l=list(map(int,input().split()))
m=max(l)
m1=min(l)
l1=[]
for i in l:
    if i!=m and i!=m1:
        l1.append(i)
print(format(sum(l1)/len(l1),".5f"))
        