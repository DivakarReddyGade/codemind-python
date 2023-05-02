n=int(input())
s=0
n1=n
while n>0:
    s=s*10+(n%10)
    n=n//10
if(s==n1):
    print("True")
else:
    print("False")