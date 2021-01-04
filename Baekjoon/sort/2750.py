n = int(input())
arr = []
 
for i in range(0, n):
    arr.append(int(input()))
 
arr.sort()
 
for j in range(0, n):
    print(arr[j])
