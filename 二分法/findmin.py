    
### one code one day
### 2020/03/07
### leetcode 153 二分法

def findMin(self, nums: List[int]) -> int:
    start = 0
    end = len(nums)-1
    if(nums[start] < nums[end]):
        return nums[0]
    else:
        while(start < end - 1):
            mid = int((start+end)/2)
            if(nums[mid] >= nums[start]):
                start = mid
            else:
                end = mid
        return nums[end]