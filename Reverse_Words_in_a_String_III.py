s=input()
a=s.split(" ")
a1=[]
for i in a:
    a1.append(i[::-1])
print(" ".join(a1))