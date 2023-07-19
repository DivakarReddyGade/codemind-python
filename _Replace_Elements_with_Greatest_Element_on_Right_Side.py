n=int(input())
l=list(map(int,input().split()))
for i in range(len(l)):
    if(i==len(l)-1):
        print("-1",)
        break
    print(max(l[i+1:len(l):1]),end=' ')