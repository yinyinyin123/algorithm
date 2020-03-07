
### by YZB at 02/20/2020 

# 给定正序序的数组和目标值，返回目标值在数组中下标，如果存在多个目标值，任意返回一个
def binary_search_target(sorted_array, target):
	# 头指针
	start = 0
	# 尾指针
	end = len(sorted_array) - 1
	# 注意边界条件
	while(start <= end):
		mid = start + int((end - start) / 2)
		if(sorted_array[mid] == target):
			return mid,sorted_array[mid]
		elif(sorted_array[mid] > target):
			end = mid - 1
		else:
			start = mid + 1
	return -1, None

# 给定正序序的数组和目标值，返回目标值在数组中下标，如果存在多个目标值，返回第一个出现的目标值下标
def binary_search_the_first_target(sorted_array, target):
	#判断第一个位置是否为target
	if(sorted_array[0] == target):
		return 0
	# 头指针，记录小于target的位置
	start = 0
	# 尾指针，记录大于等于target的位置
	end = len(sorted_array) - 1
	# 注意边界条件
	while(start < end - 1):
		mid = start + int((end - start) / 2)
		if(sorted_array[mid] >= target):
			end = mid
		else:
			start = mid
	return start + 1

# 给定正序序的数组和目标值，返回目标值在数组中下标，如果存在多个目标值，返回最后一个出现的目标值下标
def binary_search_the_last_target(sorted_array, target):
	# 判断最后一个位置是否为target
	if(sorted_array[-1] == target):
		return len(sorted_array) - 1
	# 头指针，记录小于等于target的位置
	start = 0
	# 尾指针，记录大于target的位置
	end = len(sorted_array) - 1
	# 注意边界条件
	while(start < end - 1):
		mid = start + int((end - start) / 2)
		if(sorted_array[mid] <= target):
			start = mid
		else:
			end = mid
	return end - 1

def test():
	pass


