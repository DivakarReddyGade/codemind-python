n=int(input())
l=list(map(str,input().split()))
c=0
for i in range(len(l)):
    if(len(l[i])%2==0):
        c+=1
print(c)