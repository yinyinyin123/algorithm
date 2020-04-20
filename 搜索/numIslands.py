
### one code one day
### 2020/04/20
### leetcode 200 岛屿数量

### 深度优先遍历 解决
def numIslands(self, grid: List[List[str]]) -> int:
    def DFS(i, j):
        if(0 <= i < row and 0 <= j < col and grid[i][j] == '1'):
            grid[i][j] = '0'
            DFS(i-1, j)
            DFS(i+1, j)
            DFS(i, j-1)
            DFS(i, j+1)
    row = len(grid)
    if(row == 0):
        return 0
    col = len(grid[0])
    res = 0
    stack = []
    for i in range(row):
        for j in range(col):
            if(grid[i][j] == '1'):
                res += 1
                DFS(i, j)
    return res
