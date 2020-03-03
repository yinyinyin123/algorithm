
### one code one day
### 2020/03/03
### leetcode 27 移除元素
### 双指针之换位指针 牛皮

def removeElement(self, nums: List[int], val: int) -> int:
    count_val = 0
    for i in range(len(nums)):
        if(nums[i] == val):
            count_val += 1
        else:
            nums[i-count_val] = nums[i]
    return len(nums)-count_val

def test():
	pass