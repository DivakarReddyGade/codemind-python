n=int(input())
l=list(map(int,input().split()))
c=0
l1=[]
for i in range(len(l)):
    c=0
    for j in range(len(l)):
        if(l[i]==l[j]):
            c+=1
    if(c==1):
        l1.append(l[i])
if(len(l1)==0):
    print('-1')
else:
    print(max(l1))