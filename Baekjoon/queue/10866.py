from collections import deque
import sys

input = sys.stdin.readline
num = int(input())
dq = deque(list())
for i in range(num):
    req = input().split(" ")
    if req[0] == "push_back":
        dq.append(req[1])
    elif req[0] == "push_front":
        dq.appendleft(req[1])
    elif req[0] == "pop_front":
        if len(dq) > 0: print(dq.popleft())
        else: print('-1')
    elif req[0] == "pop_back":
        if len(dq) > 0: print(dq.pop())
        else: print('-1')
    elif req[0] == "front":
        if len(dq) > 0: print(dq[0])
        else: print('-1')
    elif req[0] == "back":
        if len(dq) >0:print(dq[-1])
        else: print('-1')
    elif req[0] == "size":
        print(len(dq))
    elif req[0] == "empty":
        print(0 if len(dq) > 0 else 1)
