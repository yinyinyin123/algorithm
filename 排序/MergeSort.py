


def merge(list1, list2):
    left = 0
    right = 0
    result = []
    while(left < len(list1) and right < len(list2)):
        if(list1[left] < list2[right]):
            result.append(list1[left])
            left += 1
        else:
            result.append(list2[right])
            right += 1
    if(left == len(list1)):
        result.extend(list2[right:])
    else:
        result.extend(list1[left:])
    return result

def mergesort(list):
    if(len(list) <= 1):
        return list
    else:
        print(1)
        mid = len(list) // 2
        list1 = mergesort(list[:mid])
        list2 = mergesort(list[mid:])
        return merge(list1, list2)

print(mergesort([10,3,5,6,1,2,11,10,10]))
