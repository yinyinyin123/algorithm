
### one code one day
### 2020/03/20
### 面试题40 最小的K个数

def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
    def partition(start, end):
        small = start - 1
        for i in range(start, end):
            if(arr[i] < arr[end]):
                small += 1
                arr[small], arr[i] = arr[i], arr[small]
        small += 1
        arr[small], arr[end] = arr[end], arr[small]
        return small
    def K_max(start, end):
        if(start < end):
            index = partition(start, end)
            if(index == k - 1):
                return index
            elif(index > k - 1):
                return K_max(start, index-1)
            else:
                return K_max(index + 1, end)
        else:
            return start
    if(k == 0):
        return []
    if(k == len(arr)):
        return arr
    index = K_max(0, len(arr)-1)
    return arr[:index+1]
