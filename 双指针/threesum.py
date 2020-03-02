
### one code one day
### 2020/03/02
### leetcode 15 三数之和
### 双指针之左右指针 牛皮

### 排序 + 双指针
### 排序可以更方便的去除重复结果并使用双指针，方便的移动指针
def threeSum(self, nums: List[int]) -> List[List[int]]:
    if(len(nums) < 3):
        return []
    else:
        answer = []
        # 排序
        nums.sort()
        for i in range(len(nums)):
            if(nums[i] > 0):
                return answer
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            # 左右指针
            L = i + 1
            R = len(nums) - 1
            while(L < R):
                if(nums[i] + nums[L] + nums[R] == 0):
                    answer.append([nums[i],nums[L],nums[R]])
                    # 去重复
                    while(L < R and nums[L] == nums[L+1]):
                        L = L + 1
                    while(L < R and nums[R] == nums[R-1]):
                        R = R - 1
                    L = L + 1
                    R = R - 1
                # 双指针改变方式
                elif(nums[i] + nums[L] + nums[R] > 0):
                    R = R - 1
                else:
                    L = L + 1
        return answer

def test():
	pass