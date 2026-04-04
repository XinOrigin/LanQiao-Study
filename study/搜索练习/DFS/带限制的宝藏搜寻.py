import sys
input = lambda : sys.stdin.readline().strip()
sys.setrecursionlimit(2000)
max_coins = 0
step = 0
ans=0
n,m = map(int,input().split())
visited = [[False] * m for _ in range(n)]
grid = [list(map(int,input().split())) for _ in range(n)]
all = 4
def dfs(x,y):
    global step,max_coins,ans
    max_coins = max(ans,max_coins)
    if step == all:
        return 
    visited [x][y] =True
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    for i in range(4):
        nx,ny= x+dx[i] , y+dy[i]

        if 0<= nx < n and 0<= ny < m and visited [nx][ny] == False and grid[nx][ny] != 1:
            has_coin = False
            if grid[nx][ny] == 2:
                ans +=1
                has_coin = True
                
                
            step +=1
            if 0< step <= all:
                dfs(nx,ny)
            if has_coin:
                ans -=1
                
                
            
            step -=1
            
            
    visited [x][y] =False
dfs(0, 0)
print(step,max_coins)


    


'''
在一个 $5 \times 5$ 的金币地图中（0 是空地，1 是墙，2 是金币），你从 (0,0) 出发，最多只能走 10 步。
请问你最多能收集到多少个金币？
'''