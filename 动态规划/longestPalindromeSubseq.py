
### one code one day
### 2020/03/10
### leetcode 516 最长回文子序列
### 动态规划
### 定义dp[i][j]为字符串i到j位置的最长回文子序列长度
### 转移方程 dp[i][j] = dp[i+1][j-1] + 2             s[i] == s[j]
###                  = max(dp[i][j-1], dp[i+1][j])  s[i] != s[j] 
### 时间复杂度O(n2) 空间复杂度O(n2)

def longestPalindromeSubseq(self, s: str) -> int:
    if(not s):
        return 0
    K = 1
    helper = [[1] * len(s) for _ in range(len(s))]
    ### 对角线式前进的动规
    while( K < len(s)):
        for i in range(len(s)-K):
            j = i + K
            ### 左右是否相等，确定如何转移
            if(s[i] == s[j]):
                if(j == i + 1):
                    helper[i][j] = 2
                else:
                    helper[i][j] = 2 + helper[i+1][j-1]
            else:
                helper[i][j] = max(helper[i][j-1],helper[i+1][j])
        K += 1
    return helper[0][len(s)-1]