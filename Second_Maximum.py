n=int(input())
for i in range(n):
    l=list(map(int,input().split()))
    l.remove(max(l))
    print(max(l))