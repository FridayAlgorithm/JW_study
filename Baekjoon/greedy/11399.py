n = int(input())
waiting = list(map(int, input().split()))
waiting.sort()
total=0
spent=0
for i in waiting:
  spent += i
  sum += spent
print(sum)
