s=input()
c=0
for i in range(len(s),0,-1):
    for j in range(len(s)-i+1):
        a=s[j:j+i]
        for k in a:
            if k not in 'aeiou':
                break
        else:
            print(len(a))
            c=1
            break
    if(c==1):
        break
            