
### 阿里笔试第二题
### 哭晕在厕所 下标写错了

matrix = []
strs = ['CCCS', 'SSSS', 'CSCS', 'SSCC']

m = 4
n = 4
walked = [[False]*m for _ in range(n)]
for i in range(len(strs)):
    matrix.append(list(strs[i]))

def getdaijia(i, j, i1, j1):
    if(matrix[i][j] == 'S' and matrix[i1][j1] == 'S'):
        return 2
    elif(matrix[i][j] == 'C' and matrix[i1][j1] == 'C'):
        return 3
    return 5

def valid(i, j, m, n):
    if(i < 0 or i >= m or j < 0 or j >= n):
        return False
    return True


def backtrack(x, y, endx, endy, daijia, m, n):
    if(x == endx and y == endy):
        global res
        res = min(res, daijia)
    elif(walked[x][y]):
        return
    else:
        walked[x][y] = True
        x1, y1 = x, y - 1
        if(valid(x1, y1, m, n)):
            temp = getdaijia(x, y, x1, y1)
            backtrack(x1, y1, endx, endy, daijia+temp, m, n)
        x1, y1 = x, y + 1
        if(valid(x1, y1, m, n)):
            temp = getdaijia(x, y, x1, y1)
            backtrack(x1, y1, endx, endy, daijia+temp, m, n)
        x1, y1 = x + 1, y
        if(valid(x1, y1, m, n)):
            temp = getdaijia(x, y, x1, y1)
            backtrack(x1, y1, endx, endy, daijia+temp, m, n)
        x1, y1 = x - 1, y
        if(valid(x1, y1, m, n)):
            temp = getdaijia(x, y, x1, y1)
            backtrack(x1, y1, endx, endy, daijia+temp, m, n)
        walked[x][y] = False

res = float('inf')
backtrack(2,0,0,2,0,m,n)
print(res)
