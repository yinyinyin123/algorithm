
### one code one day
### 2020/04/12
### leetcode 494 目标和

### 转换为 01背包问题

def findTargetSumWays(self, nums: List[int], S: int) -> int:
    arrSum = sum(nums)
    if(arrSum < S or arrSum < (-1) * S):
        return 0
    else:
        ### 巧妙 再次分析
        if((arrSum + S) % 2 == 0):
            target = (arrSum + S) // 2
        else:
            return 0
        ### 01背包 DP走起
        dp = [0] * (1 + target)
        dp[0] = 1
        for i in range(len(nums)):
            for j in range(target, nums[i]-1, -1):
                dp[j] = dp[j] + dp[j-nums[i]]
        return dp[-1]
