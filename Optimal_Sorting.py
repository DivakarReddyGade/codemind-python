n=int(input())
for i in range(n):
    m=int(input())
    l=list(map(int,input().split()))
    if(sorted(l)==l):
        print('0')
    else:
        print(max(l)-min(l))