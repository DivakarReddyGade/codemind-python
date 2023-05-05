n=int(input())
l=list(map(int,input().split()))
a=sum(l)//len(l)
if a in l:
    print("True")
else:
    print("False")