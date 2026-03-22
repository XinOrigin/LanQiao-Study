class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i==j:continue
                if nums[i]+nums[j] == target:
                    return [i,j]

#暴力方法

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return [i,j]
#暴力方法优化（剔除重复）
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i,x enumerate(nums):
            if d.get(target-x) is not none:
                return [x,target-x]
        d[x] =i
#hash 思想字典查找









'''给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target  的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

 

示例 1：

输入：nums = [2,7,11,15], target = 9
输出：[0,1]
解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。
示例 2：

输入：nums = [3,2,4], target = 6
输出：[1,2]
示例 3：

输入：nums = [3,3], target = 6
输出：[0,1]
 

提示：

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
只会存在一个有效答案
 

进阶：你可以想出一个时间复杂度小于 O(n2) 的算法吗？'''