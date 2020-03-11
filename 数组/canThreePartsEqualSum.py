
### one code one day
### 2020/03/11
### leetcode 1013 将数组分成和相等的三个部分
### 利用双指针来做 O(n)
### 注意 该方法很笨
### 最优的方法：利用贪心思想，找sum / 3


def canThreePartsEqualSum(self, A: List[int]) -> bool:
    if(len(A) < 3):
        return False
    array_sum = sum(A)
    ### 左右指针
    i = 0
    j = len(A) - 1
    left_sum = A[i]
    right_sum = A[j]
    while(i <= j - 2):
        if(left_sum == right_sum):
        	### 左 = 中 = 右
            if(3 * left_sum == array_sum):
                return True
            else:
                i += 1
                j -= 1
                left_sum += A[i]
                right_sum += A[j]
        elif(left_sum < right_sum):
        	### 左 < 右 and 中 < 右
            if(array_sum - left_sum - right_sum < right_sum):
                j -= 1
                right_sum += A[j]
            ### 左 < 右 and 中 > 右
            else:
                i += 1
                left_sum += A[i]
        else:
        	### 左 > 右 and 中 < 左
            if(array_sum - left_sum - right_sum < left_sum):
                i += 1
                left_sum += A[i]
            else:
                j -= 1
                right_sum += A[j]
    return False