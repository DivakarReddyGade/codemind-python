n=int(input())
n1=n*n
s=0
while n1>0:
    s=s+n1%10
    n1=n1//10
if(s==n):
    print("Neon Number")
else:
    print("Not Neon Number")