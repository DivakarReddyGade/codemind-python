def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
n=int(input())
temp=n
rev=0
while(temp!=0):
    r=temp%10
    rev=rev*10+r
    temp=temp//10
if(prime(n) and prime(rev)):
    print("circular prime")
elif(prime(n) or prime(rev)):
    print("prime but not a circular prime")
else:
    print("not prime")