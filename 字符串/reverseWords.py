
### one code one day
### 2020/04/10
### leetcode 151 翻转字符串的单词

class Solution:
    def reverseWords(self, s: str) -> str:
        def getFirstWord(start, end):
            word = ''
            while(start < end and s[start] == ' '):
                start += 1
            while(start < end and s[start] != ' '):
                word += s[start]
                start += 1
            return word, start
        start = 0
        end = len(s)
        res = ''
        while(start < end):
            word, start = getFirstWord(start, end)
            if(word != ''):
                if(res == ''):
                    res = word
                else:
                    res = word + ' ' + res
        return res
