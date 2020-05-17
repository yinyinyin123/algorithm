
### one code one day
### 2020/05/17
### leetcode 5 最长回文子串

# 方法一 中心扩展 空间复杂度为 O(1) 时间复杂度为O(n2)
def longestPalindrome(self, s: str) -> str:
    def helper(i, j):
        while(i >= 0 and j < len(s) and s[i] == s[j]):
            i -= 1
            j += 1
        return s[i+1:j]
    if(s == ''):
        return ""
    else:
        res = s[0]
        for i in range(len(s)):
            palindRome = helper(i, i)
            if(len(palindRome) > len(res)):
                res = palindRome
            palindRome = helper(i, i+1)
            if(len(palindRome) > len(res)):
                res = palindRome
        return res

### DP: 对角线类 DP 时间复杂度和空间复杂度都为 O(n2)
def longestPalindrome(self, s: str) -> str:
    res = s[0]
    dp = [[False]*(len(s)) for _ in range(len(s))]
    for step in range(len(s)):
        for i in range(len(s)-step):
            if(step == 0):
                dp[i][i] = True
            elif(step == 1 and s[i] == s[i+1]):
                dp[i][i+1] = True
                if(len(res) < 2):
                    res = s[i:i+2]
            else:
                if(s[i] == s[i+step] and dp[i+1][i+step-1]):
                    dp[i][i+step] = True
                    if(len(res) < step + 1):
                        res = s[i:i+step+1]
    return res
