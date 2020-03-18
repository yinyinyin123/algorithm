
### one code one day
### 两个排序数组 找第 K大的数字
### 二分

def K_of_two_sorted_arr(arr1, arr2, K):
    start, end = 0, len(arr1)-1
    while(start <= end):
        mid = (start + end) // 2
        if(mid >= K):
            end = mid - 1
        elif(mid == K - 1):
            if(arr1[mid] <= arr2[0]):
                return arr1[mid]
            else:
                end = mid - 1
        else:
            arr2_idx = K - 2 - mid
            if(arr2_idx >= len(arr2)):
                start = mid + 1
                continue
            if(arr2[arr2_idx] > arr1[mid]):
                if(mid == len(arr1) - 1 or (mid != len(arr1)-1 and arr2[arr2_idx] <= arr1[mid + 1])):
                    return arr2[arr2_idx]
                else:
                    start = mid + 1
            else:
                if(arr2_idx == len(arr2) - 1 or (arr2_idx != len(arr2)-1 and arr1[mid] <= arr2[arr2_idx+1])):
                    return arr1[mid]
                else:
                    end = mid - 1
    return arr2[K-1]

arr1 = [1,4,6,10,20,25,26,30]
arr2 = [2,3,5,8,11,31]
for k in range(1,len(arr1)+len(arr2)+1):
    print(K_of_two_sorted_arr(arr1, arr2, k))
