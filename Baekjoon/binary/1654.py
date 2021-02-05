import sys
input= sys.stdin.readline
K,N = map(int,input().split())
arr = [int(input()) for _ in range(K)]
left, right = 1, max(arr)
while(left<= right):
    mid= (left+right)//2
    sum = 0
    for i in arr:
        sum += i//mid
    
    if sum >= N:  
        left = mid+1
    else : 
        right = mid-1

print(right)
