n = int(input())
sequence = list(map(int, input().split(' ')))
length = [1]*n

for i in range(1,n):
  for j in range(0,i):
    if sequence[j]<sequence[i]:
      length[i] = max( length[i], length[j]+1 )

print(max(length))
