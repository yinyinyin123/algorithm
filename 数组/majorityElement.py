
### one code one day
### 2020/03/13
### leetcode 169 多数元素

### 投票法
def majorityElement(self, nums: List[int]) -> int:
    count = 0
    majority = 0
    for num in nums:
        if(count == 0):
            count = 1
            majority = num
        else:
            if(num == majority):
                count += 1
            else:
                count -= 1
    return majority

### 中位数法
def majorityElement(self, nums: List[int]) -> int:
    ### 快排的partition
    def partition(start, end):
        small = start - 1
        for i in range(start, end):
            if(nums[i] < nums[end]):
                small += 1
                nums[small], nums[i] = nums[i], nums[small]
        small += 1
        nums[small], nums[end] = nums[end], nums[small]
        return small
    ### 找第K大元素    
    def kthMax(start, end):
        if(start < end):
            k = partition(start, end)
            if(k == K):
                return nums[k]
            elif(k < K):
                return kthMax(k+1, end)
            else:
                return kthMax(start, k-1)
        elif(start == end):
            return nums[start]
    K = len(nums) // 2
    return kthMax(0,len(nums)-1)