
### one code one day
### 2020/03/06
### leetcode 287 寻找重复数
### 快慢指针 时间复杂度O(n)

def findDuplicate(self, nums: List[int]) -> int:
    ### 快慢指针
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        ### 快指针追上慢指针一圈
        if slow == fast:
            break
    ### 找入口
    find = 0
    while True:
        find = nums[find]
        slow = nums[slow]
        if find == slow:
            return find

