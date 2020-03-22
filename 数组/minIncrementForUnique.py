
### one code one day
### 2020/03、22
### leetcode 945 使数组唯一的最小增量

### 排序 比较
def minIncrementForUnique(self, A: List[int]) -> int:
    ### 边界判定
    if(len(A) == 0 or len(A) == 1):
        return 0
    A.sort()
    res = 0
    for i in range(1,len(A)):
        if(A[i] <= A[i-1]):
            res += A[i-1] - A[i] + 1
            A[i] = A[i-1] + 1
    return res
