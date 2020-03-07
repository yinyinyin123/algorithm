
### one code one day
### 2020/02/25
### leetcode 34
### 在升序数组中查找元素的第一个和最后一个位置
### 要求时间复杂度O(lgn) 
### 我的解决方法, 只扫描一遍

def searchRange(self, nums: List[int], target: int) -> List[int]:
	# 首尾指针
    start = 0
    end = len(nums) - 1

    # 先找到第一个找到的target下标，
    target_index = -1
    while(start <= end):
        mid = int((end - start) / 2) + start
        if(nums[mid] == target):
            target_index = mid
            break
        elif(nums[mid] < target):
            start = mid + 1
        else:
            end = mid - 1

    # 判断数组中是否有target
    if(target_index == -1):
        return [-1,-1]
    else:
    	# 在start和之前找到的target下标找第一个target下标
    	# 注意判断start位置 
        if(nums[start] == target):
            target_first = start
        else:
            temp = target_index
            while(start < temp-1):
                mid = int((temp - start)/2) + start
                if(nums[mid] >= target):
                    temp = mid
                else:
                    start = mid
            target_first = start + 1

        # 在之前找到的target下标和end之间找最后一个target下标
    	# 注意判断end位置 
        if(nums[end] == target):
            target_end = end
        else:
            temp = target_index
            while(temp < end - 1):
                mid = int((end - temp)/2) + temp
                if(nums[mid] <= target):
                    temp = mid
                else:
                    end = mid
            target_end = end - 1
        return [target_first,target_end]