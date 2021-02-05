t = int(input())
horiz = [1, -1, 0, 0]
verti = [0, 0, -1, 1]
def bfs(x, y):
    queue = [[x, y]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        for i in range(4):
            y = a + horiz[i]
            x = b + verti[i]
            if 0 <= y < n and 0 <= x < m and s[y][x] == 1:
                s[y][x] = 0
                queue.append([y, x])
                //배추탐색기
for i in range(t):
    m, n, k = map(int, input().split())
    s = [[0] * m for i in range(n)]
    cnt = 0
    for j in range(k):
        a, b = map(int, input().split())
        s[b][a] = 1
        //배추심어주기
    for y in range(n):
        for x in range(m):
            if s[y][x] == 1:
                bfs(y, x)
                s[y][x] = 0
                cnt += 1
                //n m 크기 배열돌면서 배추있으면 바꾸고 카운트하기
    print(cnt)
