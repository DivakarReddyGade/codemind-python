n=int(input())
for i in range(1,n+1):
    for j in range(i,n):
        print(' ',end='')
    print((10**i//9)**2)