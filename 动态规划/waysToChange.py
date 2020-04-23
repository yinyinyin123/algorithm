
### one code one day
### 2020/04/23
### leetcode 面试题08.11硬币

### 无限背包类型
def waysToChange(self, n: int) -> int:
    if(n == 0):
        return 0
    coins = [1, 5, 10, 25]
    dp = [0] * (1 + n)
    dp[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            dp[i] += dp[i - coin]
    return dp[n] % 1000000007
