
### one code one day
### 2020/03/19
### leetcode 1027 最长等差序列

###最长子序列类 DP
def longestArithSeqLength(self, A: List[int]) -> int:
    dp = [{} for _ in range(len(A))]
    res = 1
    for i in range(len(A)):
        for j in range(i):
            num = A[i] - A[j]
            if(num in dp[j]):
                dp[i][num] = dp[j][num] + 1
            else:
                dp[i][num] = 2
            res = max(res, dp[i][num])
    return res
