import math
n=int(input())
for i in range(n):
    m=int(input())
    l=int(math.sqrt(m))
    if(l*l==m):
        print("True")
    else:
        print("False")
