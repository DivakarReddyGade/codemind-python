n=int(input())
l=list(map(int,input().split()))
import math
s=0
for i in l:
    if(int(math.sqrt(i))*int(math.sqrt(i))==i):
        s=s+i
print(s)