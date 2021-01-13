from collections import deque

from collections import deque
n = int(input())
nums = deque()

for i in range(1, n+1):
    nums.append(i)


def que():
    cnt = 0
    while(len(nums) >= 1):
        cnt += 1
        if(len(nums) == 1):
            return nums[0]

        if(cnt % 2 == 1):
            nums.popleft()

        elif(cnt % 2 == 0):
            nums.append(nums.popleft())


print(que())
#디큐안쓰면 카드배열 생성하고 하는데서 시간초과오류 오지게뜸
