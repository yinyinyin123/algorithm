
### one code one day
### 2020/03/21
### leetcode 813 最大平均值和的分组
### dp[i][k] 表示前i个元素分为k个数组的最大平均和
### dp[i][k] = max(dp[j][k-1]+average(j~i)) for j in range(1,i)

def largestSumOfAverages(self, A: List[int], K: int) -> float:
    arr_sum = [0]
    ### 记录i之前的元素和，便于后续求区间平均值
    for num in A:
        arr_sum.append(arr_sum[-1] + num)
    ### 背包类 DP
    dp = [[0]*(K+1) for _ in range(1+len(A))]
    for i in range(1, 1+len(A)):
        dp[i][1] = (arr_sum[i]) / i
        for k in range(2, 1 + min(i,K)):
            for j in range(k-1,i):
                dp[i][k] = max(dp[i][k], dp[j][k-1]+(arr_sum[i]-arr_sum[j])/(i-j))
    return dp[len(A)][K]
