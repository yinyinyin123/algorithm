
### one code one day
### 2020/03/05
### leetcode 162 寻找峰值
### 二分法 牛皮 无敌

### 仔细分析为何可以二分，深入理解二分
def findPeakElement(self, nums: List[int]) -> int:
    l, r = 0, len(nums)-1
    while(l < r):
        mid = int((l+r)/2)
        if(nums[mid] > nums[mid+1]):
            r = mid
        else:
            l = mid + 1
    return l

def test():
	pass