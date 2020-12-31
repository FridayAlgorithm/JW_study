#3키로 5키로 봉지로 최소 봉지개수 만드는 경우 찾기 프로그램 
W = int(input()) 
#배달해야할 키로수를 입력받는다
result = 0 
#결과값을 저장할 변수
while True : 
    if W % 5 == 0 : 
        result = result + (W // 5) 
        print(result) 
        break
    W -= 3
    result += 1 
    if N < 0 : 
        print(-1)
        break
