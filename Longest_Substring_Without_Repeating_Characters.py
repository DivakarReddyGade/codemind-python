s=input()
c=0
for i in range(len(s),2,-1):
    for j in range(len(s)-i+1):
        a=s[j:j+i]
        m=a.upper()
        if len(a)==len(set(m)):
            print(a)
            c=1
            break
    if c==1:
        break
if c==0:
    print("-1")
            