import math
s=int(input())
for i in range(s):
    m,n=map(int,input().split())
    c=0
    for j in range(int(math.floor(math.sqrt(m))),n//2+1):
        if(j*j)%n==m:
            print(j)
            c=1
            break
    if c==0:
        print(-1)