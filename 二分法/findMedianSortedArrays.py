
### one code one day
### 2020/03/18
### leetcode 4 寻找两个排序数组的中位数

def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
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
    if(not nums1):
        return (nums2[(len(nums2) // 2)] + nums2[(len(nums2)-1) // 2]) / 2
    elif(not nums2):
        return (nums1[(len(nums1) // 2)] + nums1[(len(nums1)-1) // 2]) / 2
    else:
        if (len(nums1) + len(nums2)) % 2 == 0:
            return K_of_two_sorted_arr(nums1, nums2, (len(nums1) + len(nums2)) // 2) / 2 + K_of_two_sorted_arr(nums1, nums2, 1 + (len(nums1) + len(nums2)) // 2) / 2
        else:
            return K_of_two_sorted_arr(nums1, nums2, 1 + (len(nums1) + len(nums2)) // 2)
