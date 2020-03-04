
### one code one day
### 2020/03/04
### leetcode 78 引申出的一种操作
### 求数组中所有的大小为K的子集
### 利用回溯法


def backtrack(first=0, cur=[]):
#	print(K)
	if(len(cur) == K):
		### 注意这句话非常关键，如果写成answer.append(cur) 会出问题，注意注意注意，分析原因
		answer.append(cur[:])
	else:
		for i in range(first, n):
			cur.append(nums[i])
			backtrack(i+1,cur)
			cur.pop()

### test 
nums = [1,2,3,4,5,6,7]
n = len(nums)
K = 4
answer = []
backtrack(0,a)
print(answer)
print(len(answer))
