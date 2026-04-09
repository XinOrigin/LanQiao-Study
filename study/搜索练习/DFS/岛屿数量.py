import sys
sys.setrecursionlimit(10000000)
input = lambda : sys.stdin.readline().strip()
M,N = map(int,input().split())
grid = [list(map(int,input().split())) for _ in range(M)]
s=0
d = [(1,0),(-1,0),(0,1),(0,-1)]
def dfs(x,y):
     for dx,dy in d:
        nx,ny = x+dx, y+dy
        if 0<= nx < M and 0<= ny < N and grid[nx][ny] == 1:
            grid[nx][ny] = 0
            dfs(nx,ny)
for i in range(M):
        for j in range(N):
            if grid[i][j] == 1:
                grid[i][j] =0
                dfs(i,j)
                s+=1
print(s)