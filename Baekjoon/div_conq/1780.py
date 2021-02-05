def check(x,y,n):
    global cnt_zero,cnt_one,cnt_minus
    tmp = s[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if tmp != s[i][j]:
                k = n//3
                check(x,y,k)
                check(x,y+k,k)
                check(x,y+2*k,k)
                check(x+k,y,k)
                check(x+k,y+k,k)
                check(x+k,y+2*k,k)
                check(x+2*k,y,k)
                check(x+2*k,y+k,k)             
                check(x+2*k,y+2*k,k)
                return
    if tmp == 0:
        cnt_zero += 1
    elif tmp == 1:
        cnt_one += 1
    else:
        cnt_minus += 1


n = int(input())
s = []
cnt_zero, cnt_one, cnt_minus = 0, 0, 0
for _ in range(n):
    s.append(list(map(int, input().split( ))))
check(0,0,n)
print(cnt_minus)
print(cnt_zero)
print(cnt_one)
