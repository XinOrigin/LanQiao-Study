#https://www.luogu.com.cn/problem/P1135


#dfs（超时）
import sys 
input = lambda : sys.stdin.readline().strip()
N,A,B = map(int,input().split())
d = [0] +list(map(int,input().split()))
step = 0
visited = [False]*(N+1)
ans = float('inf')
def dfs(l):
    global ans,step
    visited[l] = True
    if step > ans:
        return
    if l==B:
        ans = min(ans,step)
        return
    dx = [d[l],-d[l]]
    for i in range(2):
        nl = l+dx[i]
        step +=1
        if 0<nl<=N  and not visited[nl]:
            dfs(nl)
        step -=1
    visited[l] = False
dfs(A)
if ans == float('inf'):
    print(-1)
else:
    print(ans)
        

        