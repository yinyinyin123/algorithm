
### one code one day
### 2020/04/16
### leetcode 491 递增的子序列

def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    def DFS(first, cur):
        if(len(cur) >= 2):
            if(cur[-1] >= cur[-2]):
                res.append(cur[:])
            else:
                return
        dic = {}
        for i in range(first, len(nums)):
            if(nums[i] not in dic):
                cur.append(nums[i])
                DFS(i+1, cur)
                cur.pop()
                dic[nums[i]] = 1
    res = []
    DFS(0, [])
    return res
