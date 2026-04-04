grid = [
    [0, 0, 1],
    [0, 1, 0],
    [0, 0, 0]
]
n, m = 3, 3
visited = [[False] * m for _ in range(n)]
ans = 0
def dfs(x,y):
    global ans
    if x==n-1 and y==n-1 :
        return 
    visited[x][y] = True
    
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and  0<=ny<m and grid[nx][ny] == 0 and not visited[nx][ny]:
            dfs(nx,ny)
            ans +=1
            return 
    visited[x][y] = False
    
    return 
dfs(0,0)
print(ans)

