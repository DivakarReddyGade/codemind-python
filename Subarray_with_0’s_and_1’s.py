n=int(input())
c=0
a=list(map(int,input().split()))
for i in range(len(a),0,-1):
    for j in range(len(a)-i+1):
        s=a[j:j+i]
        if s.count(0)==s.count(1):
            print(j,j+i-1)
            c=1
            break
    if(c==1):
        break
else:
    print("-1")
        