n=int(input())
result=[0 for _ in range(n+1)]
 
 
def make_one(n):
    if n==1:
        return
    result[2]=1
    if n==2:
        return
    result[3]=1
    if n==3:
        return
    for i in range(4,n+1):
        result[i] = result[i - 1] + 1
        if i%3==0:
            result[i]=min(result[i//3]+1,result[i])
        if i%2==0:
            result[i]=min(result[i//2]+1,result[i])
 
make_one(n)
print(result[n])
