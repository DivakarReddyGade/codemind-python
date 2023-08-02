n=int(input())
l=list(map(int,input().split()))
l1=[]
for i in l:
    if i<0:
        i=i*(-1)
    print(len(str(i)),end=" ")