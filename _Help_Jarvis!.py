t=int(input())
for i in range(t):
    m=int(input())
    s=str(m)
    a=list(s)
    a.sort()
    c=0
    for i in range(len(a)-1):
        if abs(int(a[i])-int(a[i+1]))==1:
            c+=1
    if c==len(a)-1:
        print("YES")
    else:
        print("NO")
            
        