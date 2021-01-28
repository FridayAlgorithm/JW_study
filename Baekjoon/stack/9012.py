import sys
n = int(input())

for _ in range(n):
    line = sys.stdin.readline()
    cnt = 0
    for ch in line:
        if ch =='(':
            cnt += 1
        elif ch ==')':
             cnt -= 1
        if cnt < 0:
            print("NO")
            break
    if cnt == 0:
        print("YES")
    elif cnt>0:
        print("NO")
