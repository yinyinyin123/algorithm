
### one code one day
### 2020/03/15
### leetcode 873 最长的斐波那契子数列的长度

### 动态规划 与最长的等差子序列同类问题

def lenLongestFibSubseq(self, A: List[int]) -> int:
	### dp数组为len(A)个哈希表
    dp = [{}  for _ in range(len(A))]
    res = 2
    ### 等差子序列类似dp操作, 走起
    for i in range(len(A)):
        for j in range(i):
            if(A[i] - A[j] in dp[j]):
                dp[i][A[j]] = dp[j][A[i] - A[j]] + 1
            else:
                dp[i][A[j]] = 2
            res = max(res, dp[i][A[j]])
    return res if res > 2 else 0