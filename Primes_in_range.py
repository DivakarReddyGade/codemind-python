import math as mt
def prime(n):
    if n==0 or n==1:
        return False
    for i in range(2,int(mt.sqrt(n))+1):
        if n%i==0:
            return False
    return True
n=int(input())
m=int(input())
l=[]
for i in range(n,m+1):
    if prime(i):
        l.append(i)
print(len(l))