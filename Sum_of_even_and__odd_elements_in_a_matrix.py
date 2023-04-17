r,c=map(int,input().split())
mat=[list(map(int,input().split())) for i in range(r)]
os=0
es=0
for i in mat:
    for j in i:
        if j%2==0:
            es=es+j
        else:
            os=os+j
print(es,os)
