import sys

def draw(x,y):
    while x != 0:
         # 몫이 1인 경우
        if (x%3) == 1 and (y%3) == 1:
            sys.stdout.write(' ')
            return
        # 3으로 나누어서 위의 if문에 걸리면 그 부분도 빈칸 처리
        x = x // 3
        y = y // 3

    sys.stdout.write('*')


n = int(input())
for i in range(n):
    for j in range(n):
        draw(j,i)
    sys.stdout.write('\n')
