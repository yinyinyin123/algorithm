
### one code one day
### 2020/03/08
### leetcode 组合总和2

### 回溯法
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    def backtrack(first=0, cur=[]):
        cur_sum = sum(cur)
        if(cur_sum > target):
            return 
        if((first < len(candidates) and cur_sum + candidates[first]*(len(candidates)-first) < target)):
            return 
        if(cur_sum == target):
            answer.append(cur[:])
        else:
            idx = first
            while(idx < len(candidates)):
                count_idx = 1
                while(idx + 1 < len(candidates) and candidates[idx] == candidates[idx+1]):
                    count_idx += 1
                    idx += 1
                for j in range(1,count_idx+1):
                    cur = cur + [candidates[idx]] * j
                    backtrack(idx+1,cur)
                    cur = cur[:-j]
                idx += 1
    candidates.sort(reverse=True)
    answer = []
    backtrack()
    return answer

### 动态规划 加排序集合去重
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    dp = [None for _ in range(target+1)]
    dp[0] = [[]]
    for candidate in candidates:
        for i in range(target,candidate-1,-1):
            temp = []
            if(dp[i-candidate] != None):
                for arr in dp[i-candidate]:
                    temp.append(arr[:]+[candidate])
            if(len(temp) != 0):
                if(dp[i] == None):
                    dp[i] = temp
                else:
                    for arr in temp:
                        dp[i].append(arr[:])
    if(not dp[target]):
        return []
    for arr in dp[target]:
        arr.sort()
    for i in range(len(dp[target])):
        dp[target][i] = tuple(dp[target][i])
    
    return [list(arr) for arr in list(set(dp[target]))]