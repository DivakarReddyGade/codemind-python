def prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
            break
    else:
        return True
n=int(input())
l=list(map(int,input().split()))
c=0
for j in l:
    if j == 1:
        continue
    if prime(j):
        c+=1
print(c)