

###输入两个单调递增的链表，输出两个链表合成后的链表，当然我们需要合成后的链表满足单调不减规则。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def Merge(self, pHead1, pHead2):
    # write code here
    if(pHead1 == None):
        return pHead2
    if(pHead2 == None):
        return pHead1
    head = prev = None
    while(pHead1 and pHead2):
        if(pHead1.val >= pHead2.val):
            if(prev):
                prev.next = pHead2
            else:
                head = pHead2
            prev = pHead2
            pHead2 = pHead2.next
        else:
            if(prev):
                prev.next = pHead1
            else:
                head = prev = pHead1
            prev = pHead1
            pHead1 = pHead1.next
    if(not pHead1):
        prev.next = pHead2
    else:
        prev.next = pHead1
    return head

 def test():
 	pass