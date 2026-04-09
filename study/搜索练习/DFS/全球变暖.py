import sys
input = lambda : sys.stdin.readline().strip()
n = int(input())
grid = [ ]
vis = [[False] *n for _ in range(n)]
for _ in range(n):
    grid.append(list(input()))
d = [(1,0),(-1,0),(0,1),(0,-1)]
is_a = False
ans = 0
def dfs(x,y):
    global is_a
    vis[x][y] = True
    if grid[x+1][y] == '#' and grid[x-1][y] == '#' and grid[x][y-1] == '#' and grid[x][y+1] == '#':
        is_a =True

    for dx,dy in d:
        nx,ny =x+dx,y+dy
        if 0<= nx < n  and 0<= ny < n  and  grid[nx][ny] == '#' and not vis[nx][ny]:
            dfs(nx,ny)
c = 0
a = 0

for i in range(n):
    for j in range(n):
        if grid[i][j] == '#' and not vis[i][j]:
            c+=1
            is_a = False
            dfs(i,j)
            if is_a == True:
                a+=1
print(c-a)
