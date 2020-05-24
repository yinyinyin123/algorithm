
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

### 二刷 2020/05/24

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def helper(posi):
            start, end = 0, len(nums1) - 1
            while(end >= 0 and start < len(nums1)):
                mid = (start + end) // 2
                if(posi < mid + 1):
                    end = mid - 1
                elif(posi == mid + 1):
                    if(len(nums2) == 0 or (nums2 and nums1[posi-1] <= nums2[0])):
                        return nums1[posi-1]
                    else:
                        end = mid - 1
                elif(posi > mid + 1 and posi - 2 - mid >= len(nums2)):
                    start = mid + 1
                else:
                    nums2Posi =  posi - 2 - mid
                    if(nums1[mid] == nums2[nums2Posi]):
                        return nums1[mid]
                    elif(nums1[mid] > nums2[nums2Posi]):
                        if(nums2Posi == len(nums2) - 1 or (nums2Posi < len(nums2) - 1 and nums1[mid] <= nums2[nums2Posi+1])):
                            return nums1[mid]
                        else:
                            end = mid - 1
                    else:
                        if(mid == len(nums1) - 1 or (mid < len(nums1) - 1 and nums1[mid+1] >= nums2[nums2Posi])):
                            return nums2[nums2Posi]
                        else:
                            start = mid + 1
            if(end < 0):
                return nums2[posi-1]
            if(start >= len(nums1)):
                return nums2[posi-len(nums1)-1]
        if(len(nums1) < len(nums2)):
            nums1, nums2 = nums2, nums1
        left, right = 1 + (len(nums1) + len(nums2)) // 2, (len(nums1) + len(nums2) + 1) // 2
        if(len(nums2) == 0):
            return (nums1[left-1] + nums1[right-1]) / 2
        return (helper(left) + helper(right)) / 2
