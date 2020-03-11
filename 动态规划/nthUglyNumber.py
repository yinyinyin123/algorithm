
### one code one day
### 2020/03/11
### leetcode 263 丑数2
### 三指针

def nthUglyNumber(self, n: int) -> int:
    dp = [1] * n
    l_2, l_3, l_5 = 0, 0, 0
    for i in range(1, n):
        dp[i] = min(dp[l_2]*2,dp[l_3]*3,dp[l_5]*5)
        if(dp[l_2]*2 == dp[i]):
            l_2 += 1
        if(dp[l_3]*3 == dp[i]):
            l_3 += 1
        if(dp[l_5]*5 == dp[i]):
            l_5 += 1
    return dp[-1]