
### one code one day
### 2020/03/07
### leetcode 219 存在重复元素2
### 散列表实现滑动窗口

def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    temp = {}
    for i in range(len(nums)):
        if(nums[i] not in temp):
            temp[nums[i]] = i
        else:
            if(i - temp[nums[i]] <= k):
                return True
            else:
                temp[nums[i]] = i
    return False