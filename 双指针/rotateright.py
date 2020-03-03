
### one code one day
### 2020/03/03
### leetcode 61 旋转列表

def rotateRight(self, head: ListNode, k: int) -> ListNode:
	### 判断head是否为空和是否不用旋转
    if(not head or k == 0):
        return head

    ### 变为循环链表，并求出链表长度
    length = 1
    p = head
    while(p.next != None):
        length += 1
        p = p.next
    p.next = head
    ### 确定要找第几个节点
    m = (length - k % length) % length
    ### 开始找第m个节点
    pre = p
    i = 0
    while(i < m):
        pre = head
        head = head.next
        i += 1
    pre.next = None
    return head

def test():
 	pass