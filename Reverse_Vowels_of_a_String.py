s=input()
s1=''
s2=''
for i in s:
    if i in "aeiouAEIOU":
        s1+=i
s3=s1[::-1]
c=0
for i in s:
    if i in "aeiouAEIOU":
        s2+=s3[c]
        c+=1
    else:
        s2+=i
print(s2)
        
        