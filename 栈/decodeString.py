
### one code one day
### 2020/04/17
### leetcode 394 字符串解码

### 栈思想
def decodeString(self, s: str) -> str:
    res = ""
    stack = []
    for char in s:
        if(char == ']'):
            ### 找字符串
            temp_str = ""
            while(stack[-1] != '['):
                temp_str = stack.pop() + temp_str
            stack.pop()
            ### 找个数
            temp_num = ""
            while(len(stack) >= 1 and stack[-1] >= '0' and stack[-1] <= '9'):
                temp_num = stack.pop() + temp_num
            ### 再进栈
            for ch in temp_str * int(temp_num):
                stack.append(ch)
        else:
            stack.append(char)
    return "".join(stack)

### 2020/05/28
### 递归法
def decodeString(self, s: str) -> str:
    def find(start, end):
        count = 0
        for i in range(start, end+1):
            if(s[i] == '['):
                count += 1
            elif(s[i] == ']'):
                count -= 1
                if(count == 0):
                    return i

    def decode(start, end):
        res = ''
        i = start
        while(i <= end):
            if('0' <= s[i] <= '9'):
                strNum = ''
                while('0'<=s[i]<='9'):
                    strNum += s[i]
                    i += 1
                idx = find(i, end)
                res = res + int(strNum) * decode(i+1, idx-1)
                i = idx + 1
            else:
                res += s[i]
                i += 1
        return res
    return decode(0, len(s)-1)
