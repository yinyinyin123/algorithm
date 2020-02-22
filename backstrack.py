

#请设计一个函数，用来判断在一个矩阵中是否存在一条包含某字符串所有字符的路径。路径可以从矩阵中的任意一个格子开始，
#每一步可以在矩阵中向左，向右，向上，向下移动一个格子。如果一条路径经过了矩阵中的某一个格子，则该路径不能再进入该格子。

​
# 参数说明 matrix以字符串形式表示矩阵，rows和cols分别为矩阵的长和宽，path为要找到的路径
def hasPath(matrix, rows, cols, path):
    # write code here
    # 回溯找路径
    def find_path(i, j, Path):
        if(Path == ''):
            return True
        elif(0 <= i < rows and 0 <= j < cols and walked[i*cols+j]):
            return False
        elif(0 <= i < rows and 0 <= j < cols and matrix[i*cols+j] == Path[0]):
            walked[i*cols+j] = True
            # 属于深度优先搜索
            if(find_path(i+1,j,Path[1:])):
                return True
            if(find_path(i-1,j,Path[1:])):
                return True
            if(find_path(i,j+1,Path[1:])):
                return True
            if(find_path(i,j-1,Path[1:])):
                return True
            #别忘了 把已经走过设置回来
            walked[i*cols+j] = False
            return False
        else:
            return False
    walked = [False] * len(matrix)
    for m in range(rows):
        for n in range(cols):
            if(find_path(m,n,path)):
                return True
    return False

def test():
    pass
