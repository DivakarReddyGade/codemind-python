n=int(input())
l=list(map(int,input().split()))
s=[]
for i in l:
    if i in s:
        print(i)
    else:
        s.append(i)