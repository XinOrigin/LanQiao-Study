import sys 
input = lambda : sys.stdin.readline().strip()
write = lambda x : sys.stdout.write(str(x)+'\n')
sys.setresursionlimit(2000)
k = int(input())
data = [list(map(int,input().split())) for _ in range(4)]
ans = 0
def dfs(x,y,c):
    global ans
    if c>k:
        return
    if x==3 and y==3 :
        if c==k:
            ans+=1
        return
    for dx,dy in [(0,1)(1,0)]:
        nx,ny = x+dx,y+dy

        if nx <=4 and ny <=4:
            dfs(nx,ny,data[nx,ny])

defs(0,0,data[0,0])

print(ans)
