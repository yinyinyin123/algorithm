
### one code one day
### 2020 02 26
### leetcode 33 搜索旋转数组

def search(self, nums: List[int], target: int) -> int:	
	###  helper函数为在有序数组中 查找元素
	def helper(start, end):
	    while(start <= end):
	        mid = int((end - start) / 2) + start
	        if(nums[mid] == target):
	            return mid
	        elif(nums[mid] > target):
	            end = mid - 1
	        else:
	            start = mid + 1
	    return -1

	### 注意边界条件，如果数组为空，返回-1
	if(not nums):
	    return -1

	### 如果数组有序 直接在整个数组上进行二分查找
	if(nums[0] < nums[len(nums)-1]):
	    return helper(0,len(nums)-1)

	### 找到一个位置，该位置前后形成两个升序数组
	start = 0
	end = len(nums) - 1
	while(start < end - 1):
	    mid = int((end - start) / 2) + start
	    if(nums[mid] >= nums[0]):
	        start = mid
	    else:
	        end = mid
	### 已经得到两个有序数组，可以进行二分查找了
	if(target >= nums[0]):
	    return helper(0,start)
	else:
	    return helper(start+1,len(nums)-1) 

def test():
	pass