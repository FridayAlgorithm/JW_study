divide = input().split('-')
result = 0
for i in range(len(divide)):
    divide2 = divide2(list(map(int, divide[i].split('+'))))
    if i == 0:
        result += divide2
    else:
        result -= divide2
print(result)
