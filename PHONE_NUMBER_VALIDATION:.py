n=int(input())
s=str(n)
for i in s:
    if(s[0]==0 or len(s)!=10):
        print("Invalid")
        break
    elif(len(s)==10):
        print("Valid")
        break