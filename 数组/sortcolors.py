
### one code one day
### 2020/03/04
### leetcode 75 颜色分类
### 一遍扫描

def sortColors(self, nums: List[int]) -> None:
    start = -1
    end = len(nums)
    index = 0
    while(index < end):
        if(nums[index] == 0):
            start += 1
            if(start != index):
                nums[index],nums[start] = nums[start],nums[index]
            else:
                index += 1
        elif(nums[index] == 2):
            end -= 1
            if(end != index):
                nums[index],nums[end] = nums[end],nums[index]
            else:
                index += 1
        else:
            index += 1

### 另一种 解题思路
### 计数法，扫描一遍确定0,1,2的个数，然后重写数组
def test():
	pass