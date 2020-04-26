
### one code one day
### 2020/04/26
### 给定一个数组元素，寻找数组中索引最大的与该元素相同的下标

### 二分法
def searchLastElement(nums, target):
    if(len(nums) == 0):
        return -1
    else:
        start = 0
        end = len(nums) - 1
        if(nums[end] == target):
            return end
        else:
            while(start < end - 1):
                mid = (start + end) / 2
                if(nums[mid] <= target):
                    start = mid
                else:
                    end = mid
            return start
