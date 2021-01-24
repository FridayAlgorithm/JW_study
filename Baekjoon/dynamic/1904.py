N = int(input())
tile = [0] * 1000001
#1000000 아님주의
tile[1], tile[2] = 1, 2
for i in range(3,N+1):
    #N아님주의
    tile[i] = (tile[i-1] + tile[i-2])%15746
print(tile[N])
