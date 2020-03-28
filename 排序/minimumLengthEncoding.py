
### one code one day
### 2020/03/28
### leetcode 820 单词的压缩编码
### 逆转字符串+排序
### 其他的方法：Trie树

def minimumLengthEncoding(self, words: List[str]) -> int:
    for i in range(len(words)):
        words[i] = words[i][::-1]
    words.sort(reverse=True)
    res = len(words[0]) + 1
    for i in range(1, len(words)):
        if(words[i] != words[i-1][:len(words[i])]):
            res += len(words[i]) + 1
    return res
