def binary_search(target, start, end, datalist):
    if start > end:
        return False
    mid = (start+end)//2
    if datalist[mid] == target:
        return True
    elif datalist[mid] > target:
        return binary_search(target, start, mid-1, datalist)
    else:
        return binary_search(target, mid+1, end, datalist)


N = int(input())
A = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

A.sort()

for m in M_list:
    if binary_search(m, 0, N-1, A):
        print(1)
    else:
        print(0)
