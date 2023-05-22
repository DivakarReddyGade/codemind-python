import math
n=int(input())
l=list(map(int,input().split()))
print(math.gcd(*l))