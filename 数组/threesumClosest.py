
### one code one day
### 2020/03/08
### leetcode 16 最接近的三数之和
### 排序+左右指针 O(n2)

def threeSumClosest(self, nums: List[int], target: int) -> int:
    closest_sum = float('inf')
    nums.sort()
    for i in range(len(nums)-2):
        start = i+1
        end = len(nums)-1
        while(start < end):
            temp = nums[i] + nums[start] + nums[end]
            if(temp == target):
                return temp
            elif(temp > target):
                end -= 1
            else:
                start += 1
            if(abs(closest_sum-target) > abs(temp-target)):
                closest_sum = temp
    return closest_sum