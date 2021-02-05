n = int(input())
s = []
horiz = [1, -1, 0, 0]
verti = [0, 0, -1, 1]
//가로세로 탐색해나갈때 쓰일 좌표용
cnt = []
for i in range(n):
    s.append(list(input()))
def bfs(i, j):
    queue = [[i, j]]
    s[i][j] = "0"
    count = 1
    while queue:
        a, b = queue[0][0], queue[0][1]
        //오른쪽 아래쪽으로 탐색
        del queue[0]
        for k in range(4):
            x = a + horiz[k]
            y = b + verti[k]
            if 0 <= x < n and 0 <= y < n and s[x][y] == "1":
                //찾았다
                s[x][y] = "0"
                queue.append([x, y])
                count += 1
                //갯수증가
    cnt.append(count)
for i in range(n):
    for j in range(n):
        if s[i][j] == "1":
            bfs(i, j)
cnt.sort()
print(len(cnt))
for i in cnt:
    print(i)
