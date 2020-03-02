
### one code one day
### 2020/03/02
### leetcode 3 无重复字符的最长子串
### 滑动窗口 双指针牛皮

def lengthOfLongestSubstring(self, s: str) -> int:
    left, right = 0, 0
    max_length = 0
    window = {}
    for char in list(set(s)):
        window[char] = 0
    while(right < len(s)):
        char = s[right]
        window[char] += 1
        while(window[char] != 1):
            window[s[left]] -= 1
            left += 1
        max_length = max(right-left+1, max_length)
        right += 1
    return max_length

def test():
	pass