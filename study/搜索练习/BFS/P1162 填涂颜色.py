import sys
from collections import deque
n = int(input())
grid = [list(map(int,input().split())) for _ in range(n)]
q = deque()
for j in range(n):
    if grid[0][j] == 0:
        q.append((0,j))
        grid[0][j] = -1
    if grid[n-1][j] == 0:
        q.append((n-1,j))
        grid[n-1][j] = -1
for i in range(n):
    if grid[i][0] == 0:
        q.append((i,0))
        grid[i][0] = -1
    if grid[i][n-1] == 0:
        q.append((i,n-1))
        grid[i][n-1] = -1
d=[(0,1),(0,-1),(1,0),(-1,0)]
while q:
    x,y = q.popleft()
    for dx,dy in d:
        nx,ny = x+dx,y+dy
        if 0<=nx<n and 0<=ny<n  and grid[nx][ny] == 0:
            q.append((nx,ny))
            grid[nx][ny] = -1
for row in grid:
    print(*((2 if x == 0 else (0 if x == -1 else 1)) for x in row))
    