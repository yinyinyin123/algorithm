
### one code one day
### 2020/04/02
### leetcode 80 删除排序数组中的重复项 2

### O(n)  记录偏移位置 一遍扫描
def removeDuplicates(self, nums: List[int]) -> int:
    length = len(nums)
    ###数组长度小于3 那么直接返回结果
    if(length < 3):
        return length
    else:
        offset = 0
        for i in range(2, length):
            ### 判断是否为第三次出现
            if(nums[i] == nums[i-offset-2]):
                offset += 1
            else:
                nums[i-offset] = nums[i]
        return length-offset
