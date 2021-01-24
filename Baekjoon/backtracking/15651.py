#from itertools import product
#n,m = map(int,input().split())
#pro = product(range(1,n+1),repeat=m)
#for p in pro:
#  print(' '.join(map(str,p)))

 
n,m=map(int,input().split())
 
result=[0 for _ in range(m)]
 
def backtracking(index,n,m):
    if index==m:
        for i in result:
            print(i,end=" ")
        print()
        return
 
    for i in range(1,n+1):
        result[index]=i
        backtracking(index+1,n,m)
 
 
backtracking(0,n,m)
  
