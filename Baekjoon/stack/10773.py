import sys
n = int(sys.stdin.readline())
arr=[]
for i in range(n):
  num = int(sys.stdin.readline())
  if num==0 and len(arr) != 0:
  # 배열의 len 이 0이 아닌조건 안넣어주면 컴파일에러뜸 주의
    del arr[-1] 
  else:
    arr.append(num)
print(sum(arr))
