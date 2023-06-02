n=int(input())
l=list(map(int,input().split()))
s=0
s1=0
for i in range(n):
    if(i<n//2):
        s+=l[i]
    else:
        s1+=l[i]
print(abs(s-s1))