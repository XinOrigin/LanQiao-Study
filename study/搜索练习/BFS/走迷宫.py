from collections import deque
import sys
input = lambda : sys.stdin.readline().strip()
N,M=map(int,input().split())
grid = [[-1]*(M+1)]
for _ in range(N):
    grid.append(list(map(int,input().split())) )
q =deque()
q.append((1,1))
dist = [[-1] *(M+1) for _ in range(N+1)]
dist[1][1] =0
d =[(1,0),(-1,0),(0,1),(0,-1)]
while q:
    x,y=q.popleft()
    for dx,dy in d:
        nx,ny = x+dx,y+dy
        if 1<= nx < N+1 and 1<= ny < M+1 and dist[nx][ny] == -1 and grid[nx][ny] ==0:
            q.append((nx,ny))
            dist[nx][ny] =dist[x][y] + 1
            if (nx,ny) == (N,M):
                print(dist[nx][ny])
                sys.exit()
print(-1)


