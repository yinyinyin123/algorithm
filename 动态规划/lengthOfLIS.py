
### one code one day
### 2020/03/14
### leetcode 300 最长子序列
### 动态规划基本问题

### 2020/04/06
### 二刷
大王
### 贪心 + 二分 O(nlogn)
def lengthOfLIS(self, nums: List[int]) -> int:
    d = []
    for n in nums:
        if not d or n > d[-1]:
            d.append(n)
        else:
            if(d[0] >= n):
                d[0] = n
            else:
                ### 二分
                l, r = 0, len(d)-1
                while(l < r-1):
                    mid = (l + r) // 2
                    if(d[mid] >= n):
                        r = mid
                    else:
                        l = mid
                d[r] = n
    return len(d)

### 动态规划
def lengthOfLIS(self, nums: List[int]) -> int:
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if(nums[j] < nums[i]):
                dp[i] = max(dp[i], dp[j]+1)
    return max(dp)
