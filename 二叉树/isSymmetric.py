
### one code one day
### 2020/05/31
### leetcode 101 对称二叉树

def isSymmetric(self, root: TreeNode) -> bool:
    def isSame(left, right):
        if(not left and not right):
            return True
        elif(not left or not right):
            return False
        else:
            if(left.val == right.val):
                return isSame(left.left, right.right) and isSame(left.right, right.left)
            return False
    if(root):
        return isSame(root.left, root.right)
    return True
