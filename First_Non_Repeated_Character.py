t=int(input())
c=0
for i in range(t):
    n=int(input())
    s=input()
    for i in s:
        if s.count(i)==1:
            print(i)
            c=1
            break
    else:
        print("-1")