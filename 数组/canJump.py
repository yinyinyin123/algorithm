    
### one code one day
### 2020/03/09
### leetcode 55 跳跃游戏

### 基于贪心思想，从后向前，不断前移target位置
def canJump(self, nums: List[int]) -> bool:
    ### 边界输入判定
    if(not nums):
        return False
    ### 数组长度为1，直接返回
    if(len(nums) == 1):
        return True
    target = len(nums) - 1
    ### 从后向前，前移target
    for i in range(len(nums)-2,0,-1):
        if(nums[i] >= target - i):
            target = i
    if(nums[0] >= target):
        return True
    return False

