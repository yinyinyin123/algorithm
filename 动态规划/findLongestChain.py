
### one code one day
### 2020/03/13
### leetcode 646 最长的数对链
### 动态规划 排序加子序列
### 最高效方法对pairs[1]排序，然后贪心

def findLongestChain(self, pairs: List[List[int]]) -> int:
    if(len(pairs) < 2):
        return len(pairs)
    else:
        pairs.sort()
        dp = [1] * len(pairs)
        for i in range(1,len(pairs)):
            for j in range(i):
                if(pairs[j][1] < pairs[i][0]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)