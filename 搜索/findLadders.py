
### one code one day
### leetcode 126 单词截龙2
### 2020/06/23

### 广度优先搜索
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        se=set(wordList)
        if not endWord in se:
            return []
        def edges(word):
            arr=list(word)
            for i in range(len(arr)):
                c=arr[i]
                for j in range(97,123):
                    arr[i]=chr(j)
                    newWord=''.join(arr)
                    if newWord in se and not newWord in marked:
                        yield newWord
                arr[i]=c
        res=[]
        marked=set()
        queue=[[beginWord]]
        while queue:
            temp=[]
            found=False
            for words in queue:
                marked.add(words[-1])
            for words in queue:
                for w in edges(words[-1]):
                    v=words+[w]
                    if w == endWord:
                        res.append(v)
                        found=True
                    temp.append(v)
            if found:          #找到就不再遍历了，即使再有endWord，路径也会更长
                break
            queue=temp
        return res
