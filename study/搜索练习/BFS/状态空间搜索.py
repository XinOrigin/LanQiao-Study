import sys
from collections import deque
N,A,B,U,D = map(int,input().split())
def bfs(N,A,B,U,D):
    dist = [-1] * (N)
    dist[A] = 0
    q = deque([A])
    while q :
        d = [U,-D]
        for _ in range(len(q)):
            l = q.popleft()

            if l == B :
                return dist[l]
            
            for dl in d:
                nl = l+dl

                if 0 <= nl <N and dist[nl] ==-1  :
                    q.append(nl)
                    dist[nl] = dist[l]+1
    return -1
print(bfs(N,A,B,U,D))







'''
楼高 $N$ 层。你在 $A$ 层，想去 $B$ 层。电梯只有两个按钮：
向上跳 $U$ 层，向下跳 $D$ 层。范围：$[0, N-1]$（不能跳到 0 层或 $N+1$ 层）。求：最少按几次键。
'''