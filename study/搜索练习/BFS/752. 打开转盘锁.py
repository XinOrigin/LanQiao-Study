#https://leetcode.cn/problems/open-the-lock
import sys
from collections import deque
def get_n(i):
    res = []
    s = list(i)
    for j in range(4):
        old_char = s[j]
        s[j] = str((int(old_char)+1)%10)
        res.append(''.join(s))
        s[j] = str((int(old_char)-1+10)%10)
        res.append(''.join(s))
        s[j] =old_char
    return res
    
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead:
            return -1
        
        visited ={'0000'}
        
        q = deque([('0000',0)])
        while q:
                x,s = q.popleft()
                if x == target:
                    return s
                for nx in get_n(x):
                    if nx not in dead and nx not in visited:
                        q.append((nx,s+1))
                        visited.add(nx)
        return -1
    



#用ai想的找邻居代码
        
#2. 状态生成小函数
# 你可以写一个辅助逻辑来生成这 8 个邻居状态。既然你决定用列表转换，代码大概长这样：

# Python
# def get_neighbors(status):
#     res = []
#     s = list(status)
#     for i in range(4): # 遍历 4 个位置
#         old_char = s[i]
#         # 向上拨
#         s[i] = str((int(old_char) + 1) % 10)
#         res.append("".join(s))
#         # 向下拨
#         s[i] = str((int(old_char) - 1 + 10) % 10)
#         res.append("".join(s))
#         # 记得恢复原样，方便下一次循环拨动另一个位置
#         s[i] = old_char
#     return res