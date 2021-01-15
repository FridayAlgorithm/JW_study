from collections import deque

N = int(input())
deque = deque([i for i in range(1, N + 1)])

while(not (len(deque) == 1)):
    deque.popleft()
    move = deque.popleft()
    deque.append(move)
    
print(deque[0])
#디큐 정의 확인
#popleft() pop()을 하되 왼쪽부터 값을 뺀다. 
#버리고 맨앞의 숫자를 뒤로 옮기기만 잘해주면 되는 문제
#디큐안쓰면 카드배열 생성하고 하는데서 시간초과오류 오지게뜸
