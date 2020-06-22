

### one code one day
### leetcode 135 分发糖果
### 2020/06/22

def candy(self, ratings: List[int]) -> int:
    N = len(ratings)
    ratings.insert(0, float('inf'))
    ratings.append(float('inf'))
    left = [1] * (N+2)
    right = [1] * (N+2)
    for i in range(2, N+1):
        if(ratings[i] > ratings[i-1]):
            left[i] = left[i-1] + 1
    for i in range(N-1, 0, -1):
        if(ratings[i] > ratings[i+1]):
            right[i] = right[i+1] + 1
    res = 0
    for i in range(1, N+1):
        res += max(left[i], right[i])
    return res
