n=int(input())
l=list(map(int,input().split()))
s=set(l)
c=0
s1=[]
for i in s:
    c=0
    for j in l:
        if(i==j):
            c+=1
    if(i==c):
        s1.append(i)
if(len(s1)==0):
    print(-1)
else:
    for i in l:
        for j in s1:
            if(i==j):
                print(j,end=' ')
                s1.remove(j)