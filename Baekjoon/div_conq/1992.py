n = int(input()) 
video = [list(input()) for _ in range(n)] 
def div(x, y, n): 
  ans = [] 
  check = True 
  color = video[x][y] 
  
  for i in range(x, x+n): 
    if not check: 
      break 
    for j in range(y, y+n): 
      if color != video[i][j]: 
        check = False 
        ans.append("(") 
        ans.extend(div(x, y, n//2)) 
        ans.extend(div(x, y+n//2, n//2)) 
        ans.extend(div(x+n//2, y, n//2)) 
        ans.extend(div(x+n//2, y+n//2, n//2))
        ans.append(")") 
        return ans 
   return color 
     
print("".join(div(0, 0, n)))
