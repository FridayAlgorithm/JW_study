#생성자 
n=int(input())
i=1
result=0
while(i<=n):
 
  s=i 
    sum=0
    while(s>0):
            sum += s%10   
            s=s//10  
    if sum+i==n:
     result=i
     break
   i+=1
 
print(result)
