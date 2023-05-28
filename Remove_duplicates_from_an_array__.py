n=int(input())
l=list(map(int,input().split()))
s=[]
c=0
for i in range(len(l)):
    s.append(-1)
for i in range(len(l)):
    c=1
    for j in range(i+1,len(l)):
        if(l[i]==l[j]):
            c+=1
            s[j]=0
    if(s[i]!=0):
        s[i]=c
for i in range(len(l)):
    if(s[i]!=0):
        print(l[i],end=' ')
            
    