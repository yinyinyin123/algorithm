
### one code one day
### 2020/05/25
### leetcode 1012 至少有1位重复数字

class Solution:
    def numDupDigitsAtMostN(self, N: int) -> int:
        digits = []
        M = N
        while(M >= 1):
            digits.insert(0, M % 10)
            M //= 10
        Dp = {}
        def DFS(posi, mask, lead, limit):
            if(posi >= len(digits)):
                return 1 if not lead else 0
            else:
                if(not limit and not lead and str(posi)+'mask'+str(mask) in Dp):
                    return Dp[str(posi)+'mask'+str(mask)]
                up = 9 if not limit else digits[posi]
                temp = 0
                for i in range(up+1):
                    if((1 << i) & mask == 0):
                        if(lead and i == 0):
                            temp += DFS(posi+1, 0, True, False)
                        else:
                            temp += DFS(posi+1, (1 << i) | mask, False, limit and i == up)
                if(not lead and not limit):
                    Dp[str(posi)+'mask'+str(mask)] = temp
                return temp
        return N - DFS(0, 0, True, True)
