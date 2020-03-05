
### one code one day
### 2020/03/05
### leetcode 189 旋转数组
### 三重转置=====旋转 牛皮

def rotate(self, nums: List[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    def reverse(i, j):
        while(i < j):
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
    k = k % len(nums)
    ### 三重转置
    reverse(0,len(nums)-1-k)
    reverse(len(nums)-k,len(nums)-1)
    reverse(0,len(nums)-1)

def test():
	pass
