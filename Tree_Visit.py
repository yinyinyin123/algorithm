
## one code one day
## 2020、02、24

## 树节点定义
class TreeNode:
	def __init__(self, x):
		self.val = x
		self.left = None
		self.right = None

class Tree:
	def __init__(self):
		self.head = self.Tree_init()
    
    # 先序建立树
	def Tree_init(self):
		val = input()
		if(val != 'none'):
			temp = TreeNode(int(val))
			temp.left = self.Tree_init()
			temp.right = self.Tree_init()
			return temp
		else:
			return None

    # 前序遍历 递归
	def PreOrder_Visit(self):
		outlist = []
		def helper(root):
			if(root):
				outlist.append(root.val)
				self.PreOrder_Visit(root.left)
				self.PreOrder_Visit(root.right)
		helper(self.head)
		return outlist

	#中序遍历 递归
	def MidOrder_Visit(self):
		outlist = []
		def helper(root):
			if(root):
				self.MidOrder_Visit(root.left)
				outlist.append(root.val)
				self.MidOrder_Visit(root.right)
        helper(self.head)
        return outlist
    
    #后序遍历 递归
	def PostOrder_Visit(self):
		outlist = []
		def helper(root):
		    if(root):
			    self.PostOrder_Visit(root.left)
			    self.PostOrder_Visit(root.right)
			    outlist.append(root.val)
		helper(self.head)
		return outlist
    
    #层次遍历  队列 注意队列实现
	def LevelOrder_Visit(self):
		outlist = []
		queue = [self.head]
		while(queue and self.head):
			root = queue[0]
			outlist.append(root.val)
			if(root.left):
				queue.append(root.left)
			if(root.right):
				queue.append(root.right)
			queue.pop(0)
		return outlist
