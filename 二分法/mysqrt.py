
### one code one day
### 2020/05/09
### leetcode 69 x的平方根

### 利用二分法
def mySqrt(self, x: int) -> int:
    if(x == 0 or x == 1):
        return x
    else:
        start = 0
        end = 1 + (x // 2)
        while(start < end - 1):
            mid = (start + end) // 2
            if(mid * mid <= x):
                start = mid
            else:
                end = mid
        return start
