
### one code one day
### 2020/04/12
### leetcode 495 目标和

### 记忆化搜索 比背包DP慢

def findTargetSumWays(self, nums: List[int], S: int) -> int:
    def backtrack(first, target):
        if((first, target) in dp):
            return dp[(first, target)]
        else:
            count = 0
            if(target == 0):
                count += 1
            for i in range(first, len(nums)):
                if(target >= nums[i]):
                    count += backtrack(i+1, target-nums[i])
            dp[(first, target)] = count
            return count
    arrSum = sum(nums)
    if(arrSum < S or arrSum < (-1) * S):
        return 0
    else:
        if((arrSum + S) % 2 == 0):
            target = (arrSum + S) // 2
        else:
            return 0
        dp = {}
        return backtrack(0, target)
