
### one code one day
### leetcode 面试题42 连续子数组的最大和
### 2020/03/27

### DP走起

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        for i in range(1, len(nums)):
            if(nums[i-1] > 0):
                nums[i] += nums[i-1]
            res = max(res, nums[i])
        return res
