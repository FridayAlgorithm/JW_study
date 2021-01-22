from itertools import product
n,m = map(int,input().split())
pro = product(range(1,n+1),repeat=m)
for p in pro:
  print(' '.join(map(str,p)))
