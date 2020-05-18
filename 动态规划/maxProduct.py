
### one code one day
### 2020/03/11
### leetcode 152 乘积最大子序列
### 动态规划 实现的代码不是很简洁
### 维护最大的正值和最小的负值

### 二刷 2020/05/18 注意条件判断

def maxProduct(self, nums: List[int]) -> int:
	### 最大正值，最小负值
    positive = negative = None
    res = -float('inf')
    for num in nums:
        if(num == 0):
        	### 如果当前num为0，重置
            res = max(0, res)
            positive = negative = None
        elif(num > 0):
        	### 交换
            positive, negative = positive * num if positive != None else num, negative * num if negative != None else None
            res = max(positive, res)
        else:
        	### 交换
            positive, negative= negative * num if negative != None else None, positive * num if positive != None else num
            if(positive):
                res = max(positive, res)
            else:
                res = max(negative, res)
    return res
