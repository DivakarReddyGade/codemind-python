n=int(input())
l=list(map(int,input().split()))
c=0
m=0
for i in range(len(l)):
    if(l[i]==1):
        c+=1
    else:
        if(m<c):
            m=c
        c=0
if(m<c):
    m=c
print(m)