#https://www.luogu.com.cn/problem/P1746
import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()
n = int(input())
grid = [[0] * (n + 1)] 
#无空格输入有问题
for _ in range(n):
    # 2. strip() 去掉换行符，直接遍历字符串中的每个字符 c
    # [0] 是为了让列指标也对齐到 1~n
    row = [0] + [c for c in input()]
    grid.append(row)
sx,sy,fx,fy = map(int,input().split())
dist = [[-1] *(n+1) for _ in range(n+1)] 
q = deque()
q.append((sx,sy))
res = float(9999999)
d = [(0,1),(0,-1),(1,0),(-1,0)]
def bfs(n,grid,sx,sy,fx,fy):
    dist[sx][sy] = 0
    while q:
        for _ in range(len(q)):
            x,y = q.popleft()
        
            for dx,dy in d :
                nx,ny = x+dx,y+dy

                if 0<nx<=n and 0<ny<=n and dist[nx][ny] == -1 and grid[nx][ny] == '0':
                    if (nx,ny) == (fx,fy) :
                        print(dist[x][y] + 1)
                    sys.exit()
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))
bfs(n,grid,sx,sy,fx,fy)



