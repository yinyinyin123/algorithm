
### one code one day
### 2020/04/10
### leetcode 109 有序链表转换二叉搜索树

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def helper(start, end):
            if(start == None):
                return None
            if(start == end):
                return None
            ### 查找链表长度为一般的节点，快慢指针法
            slow = fast = start
            while(fast != end and fast.next != end):
                slow = slow.next
                fast = fast.next.next
            node = TreeNode(slow.val)
            node.left = helper(start, slow)
            node.right = helper(slow.next, end)
            return node
        return helper(head, None)
