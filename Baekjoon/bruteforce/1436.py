n=int(input())
m=666
while(n):
    #n번째로 666포함되는걸 찾기위해 하나씩 감소해나가며 n번쨰 작은수 찾기
    if '666' in str(m):
    # : 같은 기본 문법좀 조심하자
        n -= 1
    m += 1

print(m-1)
