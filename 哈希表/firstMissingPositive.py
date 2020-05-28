
### one code one day
### 2020/05/28
### leetcode 41 缺失的第一个正数

def firstMissingPositive(self, nums: List[int]) -> int:
    if(not nums):
        return 1
    elif(len(nums) == 1):
        return 1 if nums[0] != 1 else 2
    else:
        if(len(nums) in nums):
            flag = True
        else:
            flag = False
        for i in range(len(nums)):
            if(nums[i] != '#'):
                j = nums[i]
                while(j != '#' and 0 <= j < len(nums)):
                    temp = nums[j]
                    nums[j] = '#'
                    j = temp
        for i in range(1, len(nums)):
            if(nums[i] != '#'):
                return i
        if(flag):
            return len(nums)+1
        return len(nums)
