n=int(input())
l=list(map(int,input().split()))
if l==sorted(l) and len(l)==len(set(l)):
    print("yes")
else:
    print("no")
