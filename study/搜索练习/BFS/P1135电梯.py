#https://www.luogu.com.cn/problem/P1135#ide
import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()
N,A,B = map(int,input().split())
d = [0] + list(map(int,input().split()))
def bfs(N,A,B):
    dist = [-1] *(N+1)
    dist[A] = 0
    q = deque([A])
    while q :
        for _ in range(len(q)):
            l = q.popleft()
            if l == B:
                return dist[l]

            for dl in [d[l],-d[l]]:
                nl = l+dl
                if 1<= nl < N+1 and dist[nl] == -1:
                    q.append(nl)
                    dist[nl] = dist[l] +1
    return -1
print(bfs(N,A,B))