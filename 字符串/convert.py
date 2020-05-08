
### one code one day
### 2020/05/08
### leetcode 6 Z字形变换

def convert(self, s: str, numRows: int) -> str:
    def helper(word, row, flag):
        if(word != ''):
            arr[row].append(word[0])
            if(flag):
                row += 1
                if(row == numRows-1):
                    flag = False
            else:
                row -= 1
                if(row == 0):
                    flag = True
            helper(word[1:], row, flag)
    if(numRows == 1):
        return s
    arr = [[] for _ in range(numRows)]
    helper(s, 0, True)
    res = ''
    for i in range(numRows):
        res += ''.join(arr[i])
    return res
