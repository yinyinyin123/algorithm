
### one code one day
### 2020/03/19
### leetcode 983 最低票价
### 常见动态规划
### dp[i] = min(dp[i-1]+costs[0], dp[i-7]+costs[1], dp[i-30]+costs[2])
### 该方法时间复杂度不是最优
### 参看 https://leetcode-cn.com/problems/minimum-cost-for-tickets/solution/zui-di-piao-jie-by-leetcode/

def mincostTickets(self, days: List[int], costs: List[int]) -> int:
    ###二分找前XXX天的下标
    def index(num, end):
        if(days[0] >= num):
            return -1
        else:
            start = 0
            while(start < end - 1):
                mid = (start + end) // 2
                if(days[mid] >= num):
                    end = mid
                elif(days[mid] < num):
                    start = mid
            return start
    dp = [float('inf')] * len(days)
    dp[0] = min(costs)
    for i in range(1, len(days)):
        ### 买 1天的票
        dp[i] = min(dp[i], dp[i-1] + costs[0])
        ### 买 7天的票
        index_pre7 = index(days[i]-6, i)
        if(index_pre7 == -1):
            dp[i] = min(dp[i], costs[1])
        else:
            dp[i] = min(dp[i], dp[index_pre7]+costs[1])
        ### 买 30天的票
        index_pre30 = index(days[i]-29, i)
        if(index_pre30 == -1):
            dp[i] = min(dp[i], costs[2])
        else:
            dp[i] = min(dp[i], dp[index_pre30]+costs[2])
    return dp[-1]
