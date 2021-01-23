p = [0 for i in range(101)]
#100아님주의
p[1] = 1
p[2] = 1
p[3] = 1
for i in range(0, 98):
    #97아님주의
    p[i + 3] = p[i] + p[i + 1]
n = int(input())
for i in range(n):
    n = int(input())
    print(p[n])
