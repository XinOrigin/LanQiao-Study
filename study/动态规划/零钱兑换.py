#a
def dfs(i):
    if i ==0 :return 0
    if i <0 : return float('inf')
    res = float('inf')
    for c in coins :
        res =min(res,dfs(i-c)+1) 
    return res

#b
from functools import lru_cache
import sys
sys.setrecursionslimit(100000)
@lru_cache(None)
def dfs(i):
    if i ==0 :return 0
    if i <0 : return float('inf')
    res = float('inf')
    for c in coins :
        res =min(res,dfs(i-c)+1) 
    return res

#c
import sys
input = lambda : sys.stdin.readline().strip()
coins = list(map(int,input().split()))
amount = int(input())
dp=[float('inf')]*(amount+1)
dp[0] = 0
for i in range(1,amount+1):
    for c in coins:
         if i<c:
            dp[i] = min(dp[i],dp[i-c]+1)
if dp[amount] == float('inf'):
    print(-1)
else:
    print(dp[amount]) 