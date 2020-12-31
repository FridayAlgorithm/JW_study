#피보나치 재귀함수로 
def fibonacci(num):
    if num<=1:
        return num
    return fibonacci(num-1)+fibonacci(num-2)

n=int(input())
print(fibonacci(n))
