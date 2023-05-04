n=int(input())
s=str(n)
sum=0
p=1
for i in s:
    p=p*int(i)
    sum=sum+int(i)
print(p-sum)