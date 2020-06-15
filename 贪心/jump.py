
### one code one day
### 2020/06/15
### leetcode 45 跳跃游戏2

### 贪心 O(n)
class Solution:
    def jump(self, nums: List[int]) -> int:
        start = 0
        res = 0
        while True:
            res += 1
            maxstep = 0
            for i in range(1, nums[start]+1):
                if(start+i == len(nums)-1):
                    return res
                elif(start+i < len(nums)-1):
                    if(i + nums[start+i] > maxstep):
                        maxstep = nums[start+i] + i
                        new_start = start+i
            start = new_start
