n=int(input())
l=list(map(int,input().split()))
l1=[]
c=0
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if(l[i]>l[j]):
            c+=1
    l1.append(c)
for k in l1:
    print(k,end=" ")