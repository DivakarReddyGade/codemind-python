n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in range(0,len(l),2):
    l1.extend([l[i]]*l[i+1])
print(*l1)
    
