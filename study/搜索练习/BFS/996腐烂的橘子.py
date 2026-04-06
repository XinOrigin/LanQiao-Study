#https://leetcode.cn/problems/rotting-oranges/description/
from collections import deque
import sys
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        d = [(0,-1),(0,1),(1,0),(-1,0)]
        q = deque()
        f=0
        for i in range(len(grid)):
            for j,x in enumerate(grid[i]):
                if x == 2:
                    q.append((i,j))
                if x == 1:
                        f+=1
        step = 0
        
        while q and f:
            step +=1   
            for _ in range(len(q)):
                
                x,y = q.popleft()
                for dx,dy in d:
                    nx,ny = x+dx,y+dy
                    if 0<= nx < len(grid) and 0<= ny < len(grid[0]) and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        f-=1
                        q.append((nx,ny))
            
        for i in range(len(grid)):
            for j,x in enumerate(grid[i]):
                if x == 1:
                    return -1
                    sys.exit()
        return step





