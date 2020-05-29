
### one code one day
### 2020/05/29
### leetcode 10 正则式匹配

### 记忆化搜索

def isMatch(self, s: str, p: str) -> bool:
    def helper(s1, p1):
        if((s1, p1) in Dp):
            return Dp[(s1, p1)]
        if(s1 == len(s) and p1 == len(p)):
            ismatch = True
        elif(s1 == len(s)):
            if(p1+1 < len(p) and p[p1+1] == '*'):
                ismatch = helper(s1, p1+2)
            else:
                ismatch = False
        elif(p1 == len(p)):
            ismatch = False
        else:
            if(p1+1 < len(p) and p[p1+1] == '*'):
                if(s[s1] == p[p1] or p[p1] == '.'):
                    ismatch =  helper(s1+1, p1) or helper(s1, p1+2)
                else:
                    ismatch = helper(s1, p1+2)
            elif(s[s1] == p[p1] or p[p1] == '.'):
                ismatch = helper(s1+1, p1+1)
            else:
                ismatch = False
        Dp[(s1, p1)] = ismatch
        return ismatch
    Dp = {}
    return helper(0, 0)
