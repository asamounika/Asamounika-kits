from typing import List
class Solution:
    def twoSum(self,nums,target):
        dict={}
        for i in range(len(nums)):
            rem=target-nums[i]
            if rem in dict:
                return ([dict[rem],i])
            dict[nums[i]]=i
nums = [2, 7, 11, 15]
target = 9

sol = Solution()
print(sol.twoSum(nums, target))