n=int(input())
l=list(map(int,input().split()))
c=0
l1=[]
for i in range(n):
    l1.append(-1)
for i in range(n):
    c=1
    for j in range(i+1,n):
        if(l[i]==l[j]):
            c+=1
            l1[j]=0
    if(l1[i]!=0):
        l1[i]=c
for i in range(n):
    if(l1[i]!=0):
        print(l[i],l1[i],end=' ')
            
            