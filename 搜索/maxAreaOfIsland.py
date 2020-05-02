
### one code one day
### 2020/05/02
### leetcode 695 岛屿的最大面积

### 栈实现深度优先搜索
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    stack = []
    res = 0
    rows = len(grid)
    if(rows == 0):
        return 0
    columns = len(grid[0])
    walked = [[False] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if(not walked[i][j] and grid[i][j]):
                temp_res = 0
                stack.append((i,j))
                while(stack):
                    row, column = stack.pop()
                    if(0 <= row < rows and 0 <= column < columns and grid[row][column]==1 and not walked[row][column]):
                        walked[row][column] = True
                        temp_res += 1
                        stack.extend([(row+1,column),(row-1,column),(row,column+1),(row,column-1)])
                res = max(res, temp_res)
    return res

### 递归实现
def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    def DFS(i, j):
        if(i < 0 or i >= rows or j < 0 or j >= columns):
            return 0
        elif(walked[i][j] or grid[i][j] == 0):
            return 0
        else:
            count = 1
            walked[i][j] = True
            return count + DFS(i-1, j) + DFS(i+1, j) + DFS(i, j-1) + DFS(i, j+1)
    res = 0
    rows = len(grid)
    if(rows == 0):
        return 0
    columns = len(grid[0])
    walked = [[False] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            if(not walked[i][j]):
                res = max(res, DFS(i, j))
    return res
