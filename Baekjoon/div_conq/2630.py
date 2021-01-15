import sys
n=int(sys.stdin.readline())
 
color_paper=[list(map(int,sys.stdin.readline().split())) for _ in range(n)]#x행 y열
 
white=0
blue=0
 
def div(x,y,n):
    global blue,white
    check=color_paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=color_paper[i][j]:
                div(x,y,n//2)
                div(x,y+n//2,n//2)
                div(x+n//2,y,n//2)
                div(x+n//2,y+n//2,n//2)
                return
 
 
    if check==0:
        white+=1
        return
    else:   
        blue+=1
        return
 
 
div(0,0,n)
print(white)
print(blue)
