#https://www.luogu.com.cn/problem/P1605
import sys
input  = lambda : sys.stdin.readline().strip()
N,M,T = map(int,input().split())
SX,SY,FX,FY = map(int,input().split())
grid = [[0] * M for _ in range(N) ]
visited = [[False] * M for _ in range(N)]
ans = 0
for _ in range(T):
    ix,iy = map(int,input().split())
    grid[ix-1][iy-1] = 1 
def dfs(x,y):
    global ans
    if x == FX-1 and y == FY -1:
        ans +=1
        return
    visited[x][y] = True
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if 0<= nx < N and 0<= ny < M and not visited[nx][ny] and grid[nx][ny] == 0:
            dfs(nx,ny)
    visited[x][y] = False
dfs(SX-1,SY-1)
print(ans)
        