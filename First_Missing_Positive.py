m=int(input())
a=list(map(int,input().split()))
a.sort()
k=0
f=0
for i in range(len(a)):
    if a[i]>0:
        k=i
        f=i
        break
for i in range(f+1,len(a)):
    if k+1!=a[i]:
        print(k+1)
        break
    k+=1
else:
    print(max(a)+1)
    