
### 2020/06/01
### leetcode 25 K个一组翻转链表
### one code one day

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        ### 反转链表
        def reverse(start, end):
            prev = None
            pcur = start
            end.next = None
            while(pcur):
                temp = pcur.next
                pcur.next = prev
                prev = pcur
                pcur = temp
            return prev, start

        start = end = head
        connect = res = None
        step = 0
        while(end):
            step += 1
            if(step == k):
                temp = end.next
                subhead, subtail = reverse(start, end)
                if(res):
                    connect.next = subhead
                else:
                    res = subhead
                connect = subtail
                start = end = temp
                step = 0
            else:
                end = end.next
        if(start == head):
            return head
        elif(start):
            connect.next = start
        return res
