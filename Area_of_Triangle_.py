import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
print(format(math.sqrt((s-a)*(s-b)*(s-c)*s),".2f"))