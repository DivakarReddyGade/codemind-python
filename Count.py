n=int(input())
l=list(map(int,input().split()))
c=0
c1=0
for i in range(n):
    if(l[i]%2==0):
        c+=1
for j in range(n):
    if(l[j]%2==1):
        c1+=1
print(c,c1,end=" ")