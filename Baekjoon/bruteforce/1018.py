N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
min_cnt = 64
b_start = []
w_start = []
for i in range(8):
    if i % 2 == 0:
        b_start.append(list(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']))
        w_start.append(list(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']))
    else:
        w_start.append(list(['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']))
        b_start.append(list(['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']))

for i in range(N - 7):
    for j in range(M - 7):
        w_cnt = 0
        b_cnt = 0
        for k in range(i, i + 8):
            for s in range(j, j + 8):
                if b_start[k-i][s-j] != chess[k][s]:
                    b_cnt += 1
        for k in range(i, i + 8):
            for s in range(j, j + 8):
                if w_start[k-i][s-j] != chess[k][s]:
                    w_cnt += 1
        min_cnt = min(min_cnt, min(b_cnt, w_cnt))
print(min_cnt)
