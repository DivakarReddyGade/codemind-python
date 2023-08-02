s=input()
c=0
for i in range(len(s),0,-1):
    for j in range(len(s)-i+1):
        a=s[j:j+i]
        if a==a[::-1]:
            print(a)
            c=1
            break
    if c==1:
        break
            