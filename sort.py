
### one code one day
### 各种排序


### 2020/02/29 实现快速排序

### partition算法 不仅可用于快排，还可以用于寻找第K大的数字
def partition(start,end):
	small = start - 1
	for i in range(start, end):
		if(arr[i] <= arr[end]):
			small += 1
			arr[small], arr[i] = arr[i], arr[small]
	small += 1
	arr[small], arr[end] = arr[end], arr[small]
	return small

def quicksort(start, end):
	if(start < end):
		index = partition(start, end)
		quicksort(start,index-1)
		quicksort(index+1,end)

def test():
	pass