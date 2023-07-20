n=int(input())
for i in range(n):
  m=int(input())
  fact=1
  for i in range(1,m+1):
    fact=fact*i
  print(fact)