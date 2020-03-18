
### 回溯法 一维模板
### 2020/03/18

def backtack(first = 0, cur = []):
	print(cur)
	for i in range(first, len(A)):
		cur.append(A[i])
		backtack(i+1, cur)
		cur.pop()
A = [1,2,3]
backtack()
