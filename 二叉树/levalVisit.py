
### one code one day
### 2020/05/01
### 层次遍历

### 利用队列
def levelVisit(root):
    queue = []
    queue.append(root)
    while(queue):
        root = queue[0]
        visit(root)
        if(root.left):
            queue.append(root.left)
        if(root.right):
            queue.append(root.right)
        queue.pop(0)
