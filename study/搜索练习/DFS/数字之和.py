import sys
input = lambda : sys.stdin.readline().strip()
target = int(input())
nums = list(map(int,input().split()))
res = []
def dfs(inx,ans,path):
    if ans == target:
        res.append(list(path))
        return
    
    if ans>target or inx == len(nums):
        return
    
    for i in range(inx,len(nums)):
        path.append(nums[i])
        dfs(i,ans+nums[i],path)
        path.pop()

dfs(0,0,[])
print(res)




'''
给你一个数字列表 nums = [1, 2, 3, 4, 5, 6, 7] 和一个目标值 target = 10。
请用 DFS 找出所有和为 target 的组合，每个数字只能用一次。（例如 [1, 2, 3, 4] 是一种，[3, 7] 是另一种）。
'''