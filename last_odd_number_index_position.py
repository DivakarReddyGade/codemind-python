n=int(input())
l=list(map(int,input().split()))
for i in range(0,len(l)):
    if(l[i]%2==1):
        a=i
print(a)