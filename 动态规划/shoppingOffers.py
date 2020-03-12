
### one code one day
### 2020/03/12
### leetcode 638 大礼包
### 动态规划的思想 无限背包
### 该解法不能100%通过，只考虑了2种物品的情况

def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
    ### 将单个商品加入到special
    for i in range(len(price)):
        temp = [0] * (1 + len(price))
        temp[i] = 1
        temp[-1] = price[i]
        special.insert(0, temp)
    ### 无限背包走起 正向操作
    dp = [[float('inf')]*(1+needs[1]) for _ in range(needs[0]+1)]
    dp[0][0] = 0
    for each in special:
        for j in range(each[0], 1+needs[0]):
            for k in range(each[1], 1+needs[1]):
                if(dp[j][k] - each[2] > dp[j-each[0]][k-each[1]]):
                    dp[j][k] = each[2] + dp[j-each[0]][k-each[1]]
    return dp[needs[0]][needs[1]]