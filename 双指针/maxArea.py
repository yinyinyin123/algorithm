    
### one code one day
### 2020/03/02
### leetcode 11 盛最多水的容器
### 双指针之左右指针 牛皮

def maxArea(self, height: List[int]) -> int:
    start = 0
    end = len(height) - 1
    MaxArea = 0
    while(start < end):
        MaxArea = (end - start) * min(height[start],height[end])
        if(height[start] > height[end]):
            end -= 1
        else:
            start += 1
    return MaxArea

def test():
    pass