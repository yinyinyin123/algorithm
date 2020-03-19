
### one code one day
### 2020/03/19
### leetcode 409 最长回文串

def longestPalindrome(self, s: str) -> int:
    dic = {}
    for char in s:
        if(char in dic):
            dic[char] += 1
        else:
            dic[char] = 1
    res = 0
    flag = False
    for char, count in dic.items():
        res += 2 * ( count // 2 )
        if(count % 2 != 0):
            flag = True
    return res if flag == False else res + 1
