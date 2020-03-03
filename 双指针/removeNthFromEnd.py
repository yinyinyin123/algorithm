
### one code one day
### 2020/03/02
### leetcode 19 删除链表的倒数N个节点
### 双指针之快慢指针 一遍扫描

def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
    prev = None
    fast = slow = head
    i = 0
    while(i < n):
        i += 1
        fast = fast.next
    while(fast != None):
        prev = slow
        slow = slow.next
        fast = fast.next
    if(slow == head):
        return head.next
    else:
        prev.next = slow.next
        return head

def test():
	pass