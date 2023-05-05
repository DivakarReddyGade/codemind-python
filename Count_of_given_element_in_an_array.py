n=int(input())
l=list(map(int,input().split()))
a=int(input())
c=0
for i in range(0,len(l)):
    if l[i]==a:
        c+=1
print(c)