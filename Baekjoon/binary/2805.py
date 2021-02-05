N, M = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
left = 1   
right = max(arr)  
answer= -1
while(left<=right):
    mid = (left+right)//2
    sum = 0
    for i in arr :
        if i-mid >= 0 : sum += i-mid
    if sum>=M :
        left = mid +1
    else :
        right = mid -1
print(right)
