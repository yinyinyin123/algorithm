
### one code one day
### 2020/06/17
### leetcode 76 最小覆盖子串

### 双指针法
### 滑动窗口
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        def cover(counter1, counter2):
            for char, num in counter1.items():
                if(counter2[char] < num):
                    return False
            return True
        from collections import Counter
        res = '#' * (len(s) + 1)
        counter = Counter(t)
        left = right = 0
        windows = Counter()
        while(right != len(s)):
            windows[s[right]] += 1
            if(cover(counter, windows)):
                res = s[left: right+1] if right-left+1 < len(res) else res
                while(cover(counter, windows)):
                    res = s[left: right+1] if right-left+1 < len(res) else res
                    windows[s[left]] -= 1
                    left += 1
            right += 1
        return res if len(res) != 1 +len(s) else ''
