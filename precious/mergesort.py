

arr = [3,1,1,2,5,4,2,10,41,12,51,5,4,1]

def merge(left, mid, right):
    temp = []
    l = left
    r = mid + 1
    while(l <= mid and r <= right):
        if(arr[l] <= arr[r]):
            temp.append(arr[l])
            l += 1
        else:
            temp.append(arr[r])
            r += 1
    if(l == mid+1):
        temp.extend(arr[r:right+1])
    else:
        temp.extend(arr[l:mid+1])
    for i in range(len(temp)):
        arr[left+i] = temp[i]

def mergesort(start, end):
    if(start < end):
        mid = start + (end - start) // 2
        mergesort(start, mid)
        mergesort(mid+1, end)
        merge(start, mid, end)
