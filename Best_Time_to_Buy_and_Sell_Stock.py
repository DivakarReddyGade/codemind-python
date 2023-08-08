m=int(input())
a=list(map(int,input().split()))
m=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if a[j]-a[i]>m:
            m=a[j]-a[i]
print(m)
        