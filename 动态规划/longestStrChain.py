
### one code one day
### 2020/03/09
### leetcode 1048 最长字符串链
### 动态规划 
### 思想,先按照字符串的长度进行排序，就和最长子序列问题相同
### 时间复杂度 O(n2)

def longestStrChain(self, words: List[str]) -> int:
    ### 自定义排序函数
    import functools
    def cmp1(str1, str2):
        if len(str2) > len(str1):
            return -1
        if len(str2) < len(str1):
            return 1
        return 0
    words = sorted(words, key=functools.cmp_to_key(cmp1))
    ### 判断str1是否为str2的前缀
    def is_pre(str1, str2):
        for i in range(len(str1)):
            if(str1[i] != str2[i]):
                break
        return str1[i:] == str2[i+1:] or str1[i:] == str2[i:-1]
    ### 边界判定
    if(len(words) == 0 or len(words) == 1):
        return len(words)
    ### 与最长子序列操作相同
    res = [1] * len(words)
    answer = 1
    for i in range(1,len(words)):
        for j in range(i,-1,-1):
            if(len(words[j]) == len(words[i])):
                continue
            elif(len(words[j]) + 1 == len(words[i])): 
                if(is_pre(words[j], words[i])):
                    res[i] = max(res[i], res[j]+1)
                    answer = max(res[i],answer)
            else:
                break
    return answer