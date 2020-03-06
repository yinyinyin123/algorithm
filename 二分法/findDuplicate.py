
### one code one day
### 2020/03/06
### leetcode 287 寻找重复数
### 二分法 时间复杂度O(nlgn)


def findDuplicate(self, nums: List[int]) -> int:
    def count_number(start,end):
        count = 0
        for num in nums:
            if(start<=num<=end):
                count += 1
        return count
    start = 1
    end = len(nums) - 1
    while(start < end):
        mid = int((start + end) / 2)
        if(count_number(start,mid) <= mid-start+1):
            start = mid + 1
        else:
            end = mid 
    return start