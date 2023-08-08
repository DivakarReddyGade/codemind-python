m=int(input())
a=list(map(int,input().split()))
a1=[]
for i in a:
    if i not in a1:
        a1.append(i)
a1.sort()
for i in range(1,len(a1)):
    for j in range(len(a1)-1):
        if a.count(a1[j])<a.count(a1[j+1]):
            a1[j],a1[j+1]=a1[j+1],a1[j]
print(*a1)
                