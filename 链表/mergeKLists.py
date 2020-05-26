
### one code one day
### 2020/05/26
### leetcode 23 合并K个排序链表

### 使用优先队列

class P():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __lt__(self, other):
        if self.a < other.a:
            return True
        else:
            return False
    def p(self):
        return self.a, self.b

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        import heapq
        heap = []
        for li in lists:
            if(li):
                heapq.heappush(heap, P(li.val, li))
        if(not heap):
            return None
        head = None
        while(heap):
            val, node = heapq.heappop(heap).p()
            if(not head):
                head = p = ListNode(val)
            else:
                p.next = ListNode(val)
                p = p.next
            if(node.next):
                heapq.heappush(heap, P(node.next.val, node.next))
        return head



def mergeTwoLists(L1, L2):
    if(not L1 or not L2):
        return L1 or L2
    head = None
    while(L1 and L2):
        if(L1.val >= L2.val):
            if(head):
                p.next = ListNode(L2.val)
                p = p.next
            else:
                head = p = ListNode(L2.val)
            L2 = L2.next
        else:
            if(head):
                p.next = ListNode(L1.val)
                p = p.next
            else:
                head = p = ListNode(L1.val)
            L1 = L1.next
    if(L1):
        p.next = L1
        return head
    else:
        p.next = L2
        return head
if(len(lists) == 0):
    return None
else:
    while(len(lists) > 1):
        lists.append(mergeTwoLists(lists.pop(),lists.pop()))
    return lists[0]
