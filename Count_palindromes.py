def palin(n):
    s=0
    x=n
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
    if x==s:
        return True
    else:
        return False
n=int(input())
l=list(map(int,input().split()))
c=0
for j in l:
    if palin(j):
        c+=1
print(c)
