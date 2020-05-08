
### one code one day
### 2020/05/08
### leetcode 221 最大正方形

def maximalSquare(self, matrix: List[List[str]]) -> int:
    ### 边界判定
    if(len(matrix) == 0):
        return 0
    else:
        res = 0
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                ### 简化代码
                if(i == 0 or j == 0):
                    matrix[i][j] = 1 if matrix[i][j] == '1' else 0
                    res = max(res, matrix[i][j] ** 2)
                ### 左右上下类DP
                elif(int(matrix[i][j])):
                    matrix[i][j] = 1 + min(matrix[i-1][j], matrix[i][j-1], matrix[i-1][j-1])
                    res = max(res, matrix[i][j] ** 2)
                else:
                    matrix[i][j] = 0
        return res
