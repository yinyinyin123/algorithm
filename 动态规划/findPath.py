
### one code one day
### 2020/03/16
###leetcode 576 出界的路径数
### 动态规划

def findPaths(self, m: int, n: int, N: int, i: int, j: int) -> int:
	### 统计出界个数
    def count(arr):
        cout = 0
        for i in range(m):
            cout += arr[i][0] + arr[i][n-1]
        for j in range(n):
            cout += arr[0][j] + arr[m-1][j]
        return cout
    ### 边界判定
    if(N == 0):
        return 0
    ### 两个数组互换操作
    A = [[[0]*n for _ in range(m)] for _ in range(N)]
    A[0][i][j] = 1
    res = 0
    res += count(A[0])
    ### dp走起
    for step in range(1, N):
        idx = step % 2
        for i in range(m):
            for j in range(n):
                A[idx][i][j] = 0
                if(j - 1 >= 0):
                    A[idx][i][j] += A[1-idx][i][j-1]
                if(j + 1 < n):
                    A[idx][i][j] += A[1-idx][i][j+1]
                if(i - 1 >= 0):
                    A[idx][i][j] += A[1-idx][i-1][j]
                if(i + 1 < m):
                    A[idx][i][j] += A[1-idx][i+1][j]
        res += count(A[idx])
    return res % (1000000007)