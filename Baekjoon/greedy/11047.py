num, cost = map(int, input().split())
list = []
total = 0

for i in range(num):
    list.append(int(input()))

for i in range(1, num+1):
    if cost // list[-i] > 0:
        total += cost // list[-i]
        cost = cost % list[-i]
        if cost == 0:
            break
            
print(total)
