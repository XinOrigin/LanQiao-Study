from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()
N,M,T = map(int,input().split())
SX,SY,FX,FY = map(int,input().split())
grid = [[0] * M for _ in range(N) ]
for _ in range(T):
    ix,iy=map(int,input().split())
    if (ix,iy)==(SX,SY):
        print(-1)
        sys.exit()
    grid[ix][iy] = 1
def bfs(grid,SX,SY,FX,FY):
    dist = [[-1] * M for _ in range(N)]
    dist[SX][SY] = 0
    q = deque([(SX,SY)])
    d = [(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
        
            if (x,y) == (FX,FY):
                return dist[x][y]
            for dx,dy in d:
                nx,ny = x+dx , y+dy

                if 0<= nx <N and 0<= ny <M and grid[nx][ny] != 1 and dist[nx][ny] ==-1:
                    q.append((nx, ny))
                    dist[nx][ny] = dist[x][y] + 1
        
    return -1

print(bfs(grid,SX,SY,FX,FY))







'''
题目背景：
一个 $N \times M$ 的网格，0 表示空地，1 表示障碍物。给定起点 (sx, sy) 和终点 (tx, ty)，求最少步数。
'''