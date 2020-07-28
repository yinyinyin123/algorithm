
### 剑指 38 字符串排列

def permution(s):
    def DFS(idx):
        if(idx == len(s)-1):
            res.append(''.join(s))
            return
        dic = set()
        for i in range(idx, len(s)):
            if(s[i] not in dic):
                dic.add(s[i])
                s[idx], s[i] = s[i], s[idx]
                DFS(idx+1)
                s[idx], s[i] = s[i], s[idx]
    s, res = list(s), []
    DFS(0)
    return res
print(len(permution('abvcc')))
