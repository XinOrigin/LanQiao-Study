#https://www.luogu.com.cn/problem/P1706
import sys
sys.setrecursionlimit(2000)
input = lambda : sys.stdin.readline().strip()
n = int(input())
used = [False]*(n+1)
path = []
def dfs(inx):
    if inx == n:
        print(''.join(f'{x:5d}'for x in path ))
        return
    for i in range(1,n+1):
        if not used[i]:
            path.append(i)
            used[i] =True
            dfs(inx+1)
            path.pop()
            used[i] =False
dfs(0)