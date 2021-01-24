n = int(input())
t = int(input())
s = [[0] * n for i in range(n)]
visit = [0 for i in range(n)]
for i in range(t):
    a, b = map(int, input().split())
    s[a - 1][b - 1] = 1
    s[b - 1][a - 1] = 1
def dfs(v):
    #print(v, end = ' ')
    visited[v] = True
    for e in range(n):
        if s[v][e] == 1 and if visited[e] == False:
            dfs(e)
dfs(0)
cnt = 0
for i in range(1, n):
    if visit[i] == 1:
        cnt += 1
print(cnt)
