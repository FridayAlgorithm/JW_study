#from itertools import combinations_with_replacement
#n,m = map(int,input().split())
#comb = combinations_with_replacement(range(1,n+1),m)
#for c in comb:
#  print(' '.join(map(str,c)))

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
