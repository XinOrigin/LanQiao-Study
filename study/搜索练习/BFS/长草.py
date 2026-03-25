import sys
from collections import deque
input = lambda : sys.stdin.readline().strip()
n,m=map(int,input().split()) 
g = [ [0] *m for _ in range(n)]
d = [(0,-1),(0,1),(1,0),(-1,0)]
q = deque()
for i in range(n):
  r = input()
  for j,x in enumerate(r):
    if x=='g':
      g[i][j] = 1
      q.append((i,j))
k = int(input())
while q and k:
  for _ in range(len(q)):
    x,y = q.popleft()
    for dx,dy in d:
      nx,ny= x+dx,y+dy
      if 0<= nx < n and 0<= ny < m and g[nx][ny]==0:
        g[nx][ny]=1
        q.append((nx,ny))
  k-=1
for row in g:
  print(''.join('g'if x else '.' for x in row))








'''
小明有一块空地，他将这块空地划分为 
n
n 行 
m
m 列的小块，每行和每列的长度都为 1。

小明选了其中的一些小块空地，种上了草，其他小块仍然保持是空地。

这些草长得很快，每个月，草都会向外长出一些，如果一个小块种了草，则它将向自己的上、下、左、右四小块空地扩展，

这四小块空地都将变为有草的小块。请告诉小明，
k
k 个月后空地上哪些地方有草。
'''