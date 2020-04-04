
### one code one day
### 2020/04/04
### leetcode 21 合并两个有序链表

### 时间复杂度为O(m+n)，空间复杂度为O(1) 循环实现
### 类似归并排序思想
### 不解释
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if(l1 == None):
        return l2
    if(l2 == None):
        return l1
    res = head = None
    while(l1 != None and l2 != None):
        if(l1.val >= l2.val):
            if(head == None):
                res = head = l2
            else:
                head.next = l2
                head = l2
            l2 = l2.next
        elif(l1.val < l2.val):
            if(head == None):
                res = head = l1
            else:
                head.next = l1
                head = head.next
            l1 = l1.next
    if(l1 != None):
        head.next = l1
    else:
        head.next = l2
    return res
