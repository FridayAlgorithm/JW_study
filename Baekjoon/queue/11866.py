from collections import deque
n, k = map(int, input().split())
s = deque([i for i in range(1,n+1)])
res = []
while len(s) != 1:
    for _ in range(k-1):
        s.append(s.popleft())
    res.append(s.popleft())
res.append(s[0])
print('<'+", ".join(map(str, res))+'>')
