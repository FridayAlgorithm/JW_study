import sys 
arr=[]
n=int(input())
for i in range(n):
    arr.append(int(sys.stdin.readline().rstrip()))
def QuickSort(left, right, arr):
    if(left>=right):
        return
    i = left
    j = right
    pivot = arr[(left+right)//2]
    while(i<=j):
        while(arr[i] <pivot):
            i+=1
        while(arr[j] >pivot):
            j-=1
        if(i<=j):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            i+=1
            j-=1
    QuickSort(left,j,arr)
    QuickSort(i,right,arr)
QuickSort(0, n - 1, arr)
for i in range(n):
    print(arr[i])
