def sum(str1):
    sum1=0
    for i in str1:
        if i.isdigit()==True:
            z=int(i)
            sum1=sum1+z
    return sum1
str1=input()
print(sum(str1))