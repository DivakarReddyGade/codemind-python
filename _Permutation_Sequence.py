from itertools import permutations
a,b=map(int,input().split())
c=1
s=''
for i in range(a):
    s=s+str(c)
    c+=1
c1=1
for p in permutations(s,a):
    if(c1==b):
        print(''.join(p))
        break
    c1+=1