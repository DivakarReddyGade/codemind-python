n=int(input())
l=list(map(int,input().split()))
s=set(l)
c=0
c1=0
for i in s:
    c=0
    for j in l:
        if(i==j):
            c+=1
    if(i%2==1):
        c1+=1
print(c1)