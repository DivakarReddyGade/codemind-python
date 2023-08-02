n=int(input())
l=list(map(int,input().split()))
l1=list(tuple(l))
l1.sort(reverse=True)
if l==l1:
    print("yes")
else:
    print("no")
