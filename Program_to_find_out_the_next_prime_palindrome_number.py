def prime(n):
    for i in range(2,n):
        if(n%i==0):
            return False
    else:
        return True
def prime_palindrome(n):
    temp=n+1
    while(1):
        temp1=temp
        rev=0
        while(temp1!=0):
            r=temp1%10
            rev=rev*10+r
            temp1=temp1//10
        if(rev==temp and prime(rev)):
            m=rev
            break
        else:
            temp=temp+1
    return m
n=int(input())
a=prime_palindrome(n)
print(a)