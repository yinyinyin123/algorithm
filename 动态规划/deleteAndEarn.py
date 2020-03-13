
### one code one day
### 2020/03/13
### leetcode 740 删除与获得点数 
### 动态规划 基于相邻的不可取的一种思想

def deleteAndEarn(self, nums: List[int]) -> int:
	### 边界判定
    if(not nums):
        return 0
    # 排序 重造数组[2,3,3,3,4,4] -->[2,3*3,4*2] --> [2,9,8] 相同的数字加起来
    nums.sort()
    i = 0
    num_to_idx = [nums[0]]
    for j in range(1,len(nums)):
        if(nums[j] == nums[j-1]):
            nums[i] += nums[j]
        else:
            i += 1
            nums[i] = nums[j]
            num_to_idx.append(nums[j])
    ### 打家劫舍类 DP走起
    dp = [0, nums[0]]
    for j in range(1,i+1):
        if(num_to_idx[j] == num_to_idx[j-1] + 1):
            dp.append(max(dp[j-1]+nums[j], dp[j]))
        else:
            dp.append(dp[j]+nums[j])
    return dp[-1]