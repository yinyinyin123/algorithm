### one code one day
### 2020/06/18
### leetcode 1028 从先序遍历还原二叉树

def recoverFromPreorder(self, S: str) -> TreeNode:
    def getDepthAndNum(s):
        if(s == ''):
            return None, None, None
        else:
            depth = 0
            strNum = ''
            for idx, char in enumerate(s):
                if(char == '-'):
                    depth += 1
                else:
                    break
            s = s[idx:]
            for idx1, char in enumerate(s):
                if('0' <= char <= '9'):
                    strNum += char
                else:
                    return depth, int(strNum), idx+idx1
            return depth, int(strNum), idx+idx1+1

    if(S == ''):
        return None
    else:
        headDepth, headVal, idx = getDepthAndNum(S)
        head = TreeNode(headVal)
        stack = [(headDepth, head)]
        S = S[idx:]
        while(S != ''):
            depth, val, idx = getDepthAndNum(S)
            node = TreeNode(val)
            lastdepth, lastnode = stack[-1]
            if(lastdepth + 1 == depth):
                lastnode.left = node
            else:
                while(lastdepth + 1 != depth):
                    stack.pop()
                    lastdepth, lastnode = stack[-1]
                lastnode.right = node
            S = S[idx:]
            stack.append((depth, node))
        return head
