
### one code one day
### 2020/03/13
### leetcode 650 只有两个键的键盘
### 动态规划 子序列类型
### 转移方程
### dp[i] = min(dp[j] + i // j) if (i % j == 0)

def minSteps(self, n: int) -> int:
	### 边界判定
    if(n == 0 or n == 1):
        return 0
    else:
    	### dp初始化
        dp = [float('inf')]*(1+n)
        dp[0] = 0
        dp[1] = 0
        ### dp转移
        for i in range(2,n+1):
            for j in range(1,i):
                if(i % j == 0):
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[-1]