    
### one code one day
### 2020/03/02
### leetcode 11 盛最多水的容器
### 双指针之左右指针 牛皮

def maxArea(self, height: List[int]) -> int:
    ### 左右指针
    start = 0
    end = len(height) - 1
    MaxArea = 0
    while(start < end):
        MaxArea = (end - start) * min(height[start],height[end])
        ### 小的位置向内测移动
        if(height[start] > height[end]):
            end -= 1
        else:
            start += 1
    return MaxArea

def test():
    pass