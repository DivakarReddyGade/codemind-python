n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    t=tuple(l)
    l.sort()
    if(l==list(t)):
        print('0')
    else:
        print(max(l)-min(l))
    