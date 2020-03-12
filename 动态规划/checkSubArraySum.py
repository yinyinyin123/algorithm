
### one code one day
### 2020/03/12
### leetcode 523 连续的子数组和
### 动态规划
### dp维护数组从开始位置到当前位置的和，便于求每个区间的和

def checkSubarraySum(self, nums: List[int], k: int) -> bool:
	### 边界判定
    if(len(nums) < 2):
        return False
    ### k为0时，单独处理
    if(k == 0):
        for i in range(len(nums)-1):
            if(nums[i] == 0 and nums[i+1] == 0):
                return True
        return False
    ### k为负数，转化为正数
    k = max(k, -k)
    ### 开始dp
    dp = [0] * len(nums)
    dp[0] = nums[0]
    for i in range(1,len(nums)):
        dp[i] = dp[i-1] + nums[i]
        if(dp[i] % k == 0):
            return True
        for j in range(0,i-1):
            if((dp[i] - dp[j]) % k == 0):
                return True
    return False	