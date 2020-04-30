
### one code one day
### leetcode 202 快乐数字
### 2020/02/27
### 编写一个算法来判断一个数是不是“快乐数”。

### 二刷 2020/04/30 快慢指针判断循环
### 该方法利用哈希表判断是否为无限循环
def isHappy(self, n: int) -> bool:
    temp = {}
    while(True):
        count = 0
        for char in str(n):
            count += int(char) ** 2
        n = count
        if(count == 1):
            return True
        elif(count in temp):
            return False
        else:
            temp[count] = 1

### 该方法利用快慢指针 判断是否陷入循环
def isHappy(self, n: int) -> bool:
	def square_sum(n):
	    count = 0
	    for char in str(n):
	        count += int(char)**2
	    return count
	slow = square_sum(n)
	fast = square_sum(slow)
	while(slow != fast):
	    slow = square_sum(slow)
	    fast = square_sum(square_sum(fast))
	return slow == 1
