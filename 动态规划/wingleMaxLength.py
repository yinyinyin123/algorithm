
### one code one day
### 2020/03/18
### leetcode 376 摆动序列
### 动态规划 O(n2)

### 最长子序列类DP
def wiggleMaxLength(self, nums: List[int]) -> int:
    if(len(nums) < 2):
        return len(nums)
    else:
        helper = [[1,1] for _ in range(len(nums))]
        res = 1
        ###最长子序列DP 走起
        for i in range(len(nums)):
            for j in range(i):
                if(nums[i] > nums[j]):
                    helper[i][1] = max(helper[i][1], helper[j][0] + 1)
                    res = max(res, helper[i][1])
                elif(nums[i] < nums[j]):
                    helper[i][0] = max(helper[i][0], helper[j][1] + 1)
                    res = max(res, helper[i][0])
                else:
                    continue
        return res
