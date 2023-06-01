n=int(input())
a=list(map(int,input().split()))
s=set(a)
c=0
s1=0
for i in s:
    c=0
    for j in a:
        if(i==j):
            c+=1
    if(i%2==0):
        s1+=i
print(s1)