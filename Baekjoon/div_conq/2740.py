n, m = map(int , input().split())
A=[list(map(int, input().split())) for i in range(n)]

m, k = map(int, input().split())
B=[list(map(int, input().split())) for i in range(m)]

mult = [[ 0 for a in range(n)] for b in range(k)]
for c in range(n):
  for d in range(k):
    for e in range(m):
      result[c][d] += A[c][e] * B[e][d]
      
for i in mult:
  for j in i:
    print(j, end=' ')
  print()
