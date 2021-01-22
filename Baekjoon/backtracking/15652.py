from itertools import combinations_with_replacement
n,m = map(int,input().split())
comb = combinations_with_replacement(range(1,n+1),m)
for c in comb:
  print(' '.join(map(str,c)))
