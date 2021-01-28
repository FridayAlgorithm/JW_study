n=int(input())
trisum=[]
for i in range(n):
    //괄호주의
  trisum.append(list(map(int,input().split())))

//if n=1:
//print(trisum[0])

if n>1:
  trisum[1][0] += trisum[0][0]
  trisum[1][1] += trisum[0][0]
  for i in range(2,n):
    for j in range(i+1):
                   //i아님 주의
    if j=0:
      trisum[i][0]+=trisum[i-1][0]
    elif j=i:
      trisum[i][j]+=trisum[i-1][j-1]
    else:
      trisum[i][j]+= max(trisum[i-1][j],trisum[i-1][j-1])
print(max(trisum[n-1]))

 
