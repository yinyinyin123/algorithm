
### one code one day
### 2020/04/03
### leetcode 8 字符串转换整数

### 自动机 骚操作
class Automaton:
    def __init__(self):
        self.state = 'start'
        self.sign = 1
        self.ans = 0
        self.table = {
            'start': ['start', 'signed', 'in_number', 'end'],
            'signed': ['end', 'end', 'in_number', 'end'],
            'in_number': ['end', 'end', 'in_number', 'end'],
            'end': ['end', 'end', 'end', 'end'],
        }

    def get_col(self, c):
        if c.isspace():
            return 0
        if c == '+' or c == '-':
            return 1
        if c.isdigit():
            return 2
        return 3

    def get(self, c):
        self.state = self.table[self.state][self.get_col(c)]
        if self.state == 'in_number':
            self.ans = self.ans * 10 + int(c)
            self.ans = min(self.ans, INT_MAX) if self.sign == 1 else min(self.ans, -INT_MIN)
        elif self.state == 'signed':
            self.sign = 1 if c == '+' else -1

class Solution:
    def myAtoi(self, str: str) -> int:
        automaton = Automaton()
        for c in str:
            automaton.get(c)
        return automaton.sign * automaton.ans

### 二刷自动机 2020/05/22

class Solution:
    def myAtoi(self, str: str) -> int:
        def getResult(res, sign):
            if(res * sign >= 2 ** 31):
                return 2 ** 31 - 1
            elif(res * sign < - 2 ** 31):
                return - 2 ** 31
            return res * sign
        transferTable = {
            'start': ['start', 'signed', 'number', 'end'],
            'signed': ['end', 'end', 'number', 'end'],
            'number': ['end', 'end', 'number', 'end'],
            'end': ['end', 'end', 'end', 'end']
        }
        res = 0
        sign = 1
        state = 'start'
        for char in str:
            if(char == ' '):
                state = transferTable[state][0]
            elif(char == '+' or char == '-'):
                state = transferTable[state][1]
                if(state != 'end'):
                    sign = -1 if char == '-' else 1
            elif('0' <= char <= '9'):
                res = 10 * res + int(char)
                state = transferTable[state][2]
            else:
                state = 'end'
            if(state == 'end'):
                getResult(res, sign)
        getResult(res, sign)
