k=int(input())
a=list(map(int,input().split()))
m=a[0]
for i in range(1,len(a)+1):
    for j in range(len(a)-i+1):
        if sum(a[j:j+i])>m:
            m=sum(a[j:j+i])
print(m)