
### one code one day
### 2020/03/04
### leetcode 78 子集

def subsets(self, nums: List[int]) -> List[List[int]]:
    if(not nums):
        return [[]]
    answer = [[]]
    for num in nums:
        for j in range(len(answer)):
            answer.append(answer[j]+[num])
    return answer

def test():
	pass
	