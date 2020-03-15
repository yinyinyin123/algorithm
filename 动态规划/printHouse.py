
### one code one day
### 2020/03/15
### leetcode 256 粉刷房子
### 动态规划 最基本操作-坐下

def printhHouse(costs):
	if(not costs):
	    return 0
	else:
	    for i in range(1,len(costs)):
	        costs[i][0] += min(costs[i-1][1], costs[i-1][2])
	        costs[i][1] += min(costs[i-1][0], costs[i-1][2])
	        costs[i][2] += min(costs[i-1][0], costs[i-1][1])
	    return min(costs[-1])

def backtack(first = 0, cur = []):
	print(cur)
	for i in range(first, len(A)):
		cur.append(A[i])
		backtack(i+1, cur)
		cur.pop()
A = [1,2,3]
backtack()

 