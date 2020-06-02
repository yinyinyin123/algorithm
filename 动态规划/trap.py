
### one code one day
### 2020/06/02
### leetcode 42 接雨水

### 动态规划
### 思考
### 每个位置的雨水能多少？

def trap(self, height: List[int]) -> int:
    if(len(height) <= 2):
        return 0
    left_max = [0] * len(height)
    left_max[0] = height[0]
    right_max = [0] * len(height)
    right_max[-1] = height[-1]
    for i in range(1, len(height)):
        left_max[i] = max(left_max[i-1], height[i])
    for i in range(len(height)-2,-1,-1):
        right_max[i] = max(right_max[i+1], height[i])
    res = 0
    for i in range(1,len(height)-1):
        res += min(left_max[i], right_max[i]) - height[i]
    return res
