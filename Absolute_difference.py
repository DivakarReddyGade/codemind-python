def is_prime(n):
    for i in range(2,n):
        if(n%i==0):
            return 0
    return 1
n=int(input())
l=list(map(int,input().split()))
p=1
p1=1
for i in l:
    if(is_prime(i)):
        p=p*i
    else:
        p1=p1*i
print(abs(p-p1))