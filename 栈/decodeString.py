
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
