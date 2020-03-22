
### one code one day
### 2020/03/22
### leetcode 312 戳气球
### 题解 https://leetcode-cn.com/problems/burst-balloons/solution/san-chong-jie-fa-by-jason-2-6/
### 动态规划
###自顶向下想问题 自底向上写代码

def maxCoins(self, nums: List[int]) -> int:
    ### 边界判定
    if(len(nums) == 0):
        return 0
    N = len(nums)
    dp = [[0]*(N+2) for _ in range(N+2)]
    ### 首尾插入1，便于操作
    nums.insert(0, 1)
    nums.append(1)
    for i in range(1, N+1):
        dp[i][i] = nums[i]*nums[i-1]*nums[i+1]
    step = 1
    ### 区间类DP 走对角线
    while(step <= N-1):
        for i in range(1, N-step+1):
            j = i + step
            for k in range(i,j+1):
                dp[i][j] = max(dp[i][j], dp[i][k-1]+dp[k+1][j]+nums[k]*nums[i-1]*nums[j+1])
        step += 1
    return dp[1][N]
