
### one code one day
### 2020/03/29
### 2020年百度实习生 算法岗 笔试
### 题目具体忘记了 这里只存个 代码

### 给 n 个数对， 如（10，4）, (20, 5), (50, 8), (40, 7), (30, 6)
### m回合 ，每回合抽一对，你会获得你抽到的那一对的第一个值，但是其他的数对的第一个值都要减去
### 这个抽到的数对的第二个值 比如抽到（10，4）,你会获得10分，但是剩下的数对会减去4，如果抽完（10，4）
### 剩下另4个，那么会变为（20-4，5），（50-4，8），（40-4，7），（30-4， 6）
### 求m回合所抽到的最大分数


n = int(input())
m = int(input())
a = [int(num) for num in input().split(' ')]
b = [int(num) for num in input().split(' ')]

new = []
for i in range(n):
    new.append([b[i], a[i]])
new.sort()

dp = []
for i in range(n):
    dp.append([new[i][1], new[i][0]])

for turn in range(1, m):
    for i in range(n-1, turn-1, -1):
        res = -1
        r = 0
        for j in range(turn-1, i):
            if(r < dp[j][0] - dp[j][1]):
                r = dp[j][0] - dp[j][1]
                res = j
        if(res != -1):
            dp[i][0] = new[i][1] + dp[res][0] - dp[res][1]
            dp[i][1] = new[i][0] + dp[res][1]
    print(dp)
