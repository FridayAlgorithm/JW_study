def hanoi(n, a, b, c): 
    if n == 1:
        print(a, b)
        return 
    hanoi(n - 1, a, c, b)
    print(a, b)
    hanoi(n - 1, c, b, a)
n = int(input())
result = 1
for i in range(1, n+1):
    result = result * 2
print(result - 1)
hanoi(n, 1, 3, 2)
