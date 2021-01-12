import sys
N = int(input())
stack = []

for _ in range(N):
    line = sys.stdin.readline().split()

    if line[0] == "push":
        stack.append(int(line[1]))

    elif line[0] == "pop":
        if len(stack)>0:
            print(stack[-1])
            stack.pop()
        else:
            print(-1)

    elif line[0] == "size":
        print(len(stack))

    elif line[0] == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)

    elif line[0] == "top":
        if len(stack) > 0:
            print(stack[-1])
        else:
            print(-1)
