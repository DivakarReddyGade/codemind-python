a=int(input())
b=int(input())
m=a+b
while(1):
    for i in range(2,m+1):
        if((m+1)%i==0):
            m=m+1
            break
    else:
        break
print(m+1-(a+b))