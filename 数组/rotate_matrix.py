
### one code one day
### 2020/03/08
### leetcode 48 旋转图像

def rotate(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    i, j, k = 0, len(matrix)-1, len(matrix)-1
    while(i < j):
    	### 左上角
        l_o = [i, i]
        ### 左下角
        l_d = [j, i]
        ### 右上角
        r_o = [i, j]
        ### 右下角
        r_d = [j, j]
        ### 交换
        temp = 0
        while(temp < k):
            matrix[l_o[0]][l_o[1]],matrix[l_d[0]][l_d[1]],matrix[r_o[0]][r_o[1]],matrix[r_d[0]][r_d[1]] = matrix[l_d[0]][l_d[1]],matrix[r_d[0]][r_d[1]],matrix[l_o[0]][l_o[1]],matrix[r_o[0]][r_o[1]]
            l_o[1] += 1
            l_d[0] -= 1
            r_o[0] += 1
            r_d[1] -= 1
            temp += 1
        i += 1
        j -= 1
        k -= 2