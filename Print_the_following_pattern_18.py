n=int(input())
for i in range(1,n+1):
    for j in range(i,n):
        print(' ',end='')
    s=str((10**i//9)**2)
    for k in s:
        print(chr(int(k)+64),end="")
    print('')