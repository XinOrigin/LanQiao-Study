import sys
from heapq import *
from collections import deque
input = lambda : sys.stdin.readline().strip()
def bfs():
    data = input()
    n,m = input().split()

    graph =[[] for _ in range(n+1)]
    for _ in range(m):
        u,v,w = map(int,input().split())
        graph[u].append((v,w))
        graph[v].append((u,w))

        dist = [float('inf')*(n+1)]
        dist[1] =0
        pq = [(0,1)]
        while pq:
            d,u=heappop(pq)
            if d > dist[u]:
                continue

            for v,w in graph[u]:
                if dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
                    heappush(pq, (dist[v], v))
        print(dist[1:])

bfs()


