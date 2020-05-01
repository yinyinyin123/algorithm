
### one code one day
### 2020/05/01
### leetcode 面试题目 后继者
### 后续遍历

def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
    if(root == None):
        return None
    elif(p == None):
        return None
    else:
        flag = False
        stack = []
        while(stack or root):
            while(root):
                print(root.val)
                stack.append(root)
                root = root.left
            root = stack.pop()
            if(flag == True):
                return root
            if(root == p):
                flag = True
            root = root.right
        return None
