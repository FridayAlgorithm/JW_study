import sys

input = sys.stdin.readline
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings.sort(key=lambda x: (x[1], x[0]))  
end_time = 0
answer = 0
for i in range(N):
    if meetings[i][0] >= end_time:
        answer += 1
        end_time = meetings[i][1]

print(answer)
