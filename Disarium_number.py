n=input()
s=0
a=1
for i in n:
    s=s+int(i)**a
    a+=1
if(s==int(n)):
    print("True")
else:
    print("False")