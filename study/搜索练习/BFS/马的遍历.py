#https://www.luogu.com.cn/problem/P1443#ide
import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()
n,m,sx,sy = map(int,input().split())
grid = [[-1]*m for _ in range(n)]
def bfs(grid,n,m,sx,sy):
    q = deque([(sx-1,sy-1)])
    grid[sx-1][sy-1] = 0
    step = 0
    d = [(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(-1,2),(1,-2),(-1,-2)]
    while q:
        for _ in range(len(q)):
            x,y=q.popleft()
            for dx,dy in d:
                nx,ny = x+dx,y+dy
                if 0<=nx<n and 0<=ny<m and grid[nx][ny] == -1:
                    q.append((nx,ny))
                    grid[nx][ny] = grid[x][y] +1

bfs(grid,n,m,sx,sy)
for r in grid:
    print(*r)