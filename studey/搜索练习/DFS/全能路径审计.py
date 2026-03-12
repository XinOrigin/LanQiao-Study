import sys 
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+'\n')
sys.setrecursionlimit(2000)
k = int(input().split)
data = [list(map(int,input().split())) for _ in range(4)]
ans = 0
visited = [[False] * 4 for _ in range(4)]
def dfs(x,y,c):
    global ans
    if c>k:
        return
    if x==3 and y==3 :
        if c==k:
            ans+=1
        return
    visited[x][y] = True
    for dx,dy in [(-1,0),(0,-1),(0,1),(1,0)]:
        nx,ny = x+dx,y+dy
        

        if 0<= nx <4 and 0<= ny <4 and visited[nx][ny] == False :
            dfs(nx,ny,c+data[nx][ny])
    visited[x][y] = False

dfs(0,0,data[0][0])

print(ans)
