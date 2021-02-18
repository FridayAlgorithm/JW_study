num = int(input())
sequence = list(map(int, input().split(" ")))
result = [-1 for _ in range(num)]
stack = []
stack.append(0)
i = 1
for i in range(num):
    while stack and sequence[stack[-1]] < sequence[i]:
        result[stack[-1]] = str(sequence[i])
        stack.pop()

    stack.append(i)
    i += 1

print(" ".join(result))

#runtimeerror ㄷ ㄷ ㄷ 
