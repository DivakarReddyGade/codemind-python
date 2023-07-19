n=int(input())
l=list(map(int,input().split()))
m=int(input())
for i in l:
    print(i+m>=max(l),end=" ")