
### one code one day
### 2020/03/05
### leetcode 217 存在重复元素
### 哈希表解决

def containsDuplicate(self, nums: List[int]) -> bool:
    temp = {}
    for num in nums:
        if(num in temp):
            return True
        else:
            temp[num] = 1
    return False

def test():
	pass