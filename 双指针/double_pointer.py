
### one code ond day 
### 2020/02/28
### leetcode 209 长度最小的子数组

### 双指针法
def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    Left = 0
    Sum = 0
    Answer = float('inf')
    for i in range(len(nums)):
        Sum += nums[i]
        ### 当总和大于s时，滑动窗口
        while(Sum >= s):
            Answer = min(answer,i - Left + 1)
            Sum -= nums[left]
            Left += 1   
    return Answer if Answer != float('inf') else 0

### 扫一遍加二分

def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    ### 二分找差值
    def helper(start,end,diff):
        temp = end
        ### 注意边界
        while(start < end - 1):
            mid = int((end - start)/2)+start
            if(nums[temp] - nums[mid] >= diff):
                start = mid
            else:
                end = mid
        return temp - start + 1, start
    if(not nums):
        return 0
    nums.insert(0,0)
    start = 0
    min_length = float('inf')
    ### 扫描数组
    for i in range(1,len(nums)):
        if(nums[i] >= s):
            return 1
        elif(nums[i-1]+nums[i] < s):
            nums[i] += nums[i-1]
        else:
            length,start = helper(start,i-1,s-nums[i])
            min_length = min(min_length,length)
            nums[i] += nums[i-1]
    if(min_length == float('inf')):
        return 0
    return min_length

def test():
	pass