N = int(input())

people = []
score = [1 for _ in range(N)]

for _ in range(N):
    heightweigh = list(map(int, input().split()))
    people.append(heightweigh)

for i in people:
    cnt = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            cnt+=1
    print(cnt, end=" ")
