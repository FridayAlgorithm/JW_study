n,k = map(int, input().split())

left = 1 
right = k
ans = 0

while left <= right:
  count = 0
  mid = (left+right)//2
  
  for i in range(1, n+1):
    count += min(mid//i, n)
  if(count < k):
    left = mid + 1
  else:
    ans = mid
    right = mid -1
print(ans)
