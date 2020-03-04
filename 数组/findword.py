
### one code one day
### 2020/03/04
### leetcode 79 单词搜索
### 回溯法

def exist(self, board: List[List[str]], word: str) -> bool:
    ### 回溯法
    def depthsearch(i, j, index):
        if(i < 0 or i >= len(board) or j < 0 or j >= len(board[0])):
            return False
        walked[i][j] = True
        if(board[i][j] == word[index]):
            if(index == len(word) - 1):
                return True
            else:
                if(i - 1 >= 0 and not walked[i-1][j] and depthsearch(i-1, j, index+1)):
                    return True
                if(j - 1 >= 0 and not walked[i][j-1] and depthsearch(i, j-1, index+1)):
                    return True
                if(j + 1 < len(board[0]) and not walked[i][j+1] and depthsearch(i, j+1, index+1)):
                    return True
                if(i + 1 < len(board) and not walked[i+1][j] and depthsearch(i+1, j, index+1)):
                    return True
                walked[i][j] = False
                return False
        else:
            walked[i][j] = False
            return False
    ### 边界判定
    if(len(board) == 0):
        return False
    walked = [[False] * len(board[0]) for _ in range(len(board))]
    for i in range(len(board)):
        for j in range(len(board[0])):
            if(depthsearch(i, j, 0)):
                return True
    return False

def test():
	pass