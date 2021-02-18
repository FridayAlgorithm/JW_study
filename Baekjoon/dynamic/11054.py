n = int(input())
sequence = list(map(int, input().split(' ')))
length = [1]*n
reverselength = [1]*n
sum = [0]*n

for i in range(1,n):
  for j in range(0,i):
    if sequence[j]<sequence[i]:
      length[i] = max( length[i], length[j]+1 )
for i in range(n-1,0,-1):
  for j in range(n,i,-1):
    if sequence[j]>sequence[i]:
      reverselength[i] = max( reverselength[i], reverselength[j]+1 )      
      
for i in range (1,n)
  sum[i] = length[i] + reverselength[i] -1

print(max(sum))
