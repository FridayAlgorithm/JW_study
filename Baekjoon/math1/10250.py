층과 방의갯수 그리고 n번째 방의 위치를 구하기 위해 w, h ,n을 입력받고 n번째로 선호하는 방에 대한 정보를 찾는 프로그램
T = int(input())
for i in range(T):
    h, w, n = map(int, input().split())
    if(n % h):
        room = (n % h * 100) + (int(n / h) + 1)
    else:
        room = (h * 100) + int(n / h)
    print(room)
