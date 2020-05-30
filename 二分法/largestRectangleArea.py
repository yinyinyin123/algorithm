
### one code one day
### 2020/0530
### leetcode 84 柱状图中最大的矩形

### 单调栈法
def largestRectangleArea(self, heights: List[int]) -> int:
    maxArea = 0
    stack = [-1]
    for i in range(len(heights)):
        if(stack[-1] == -1 or (stack[-1] != -1 and heights[i] > heights[stack[-1]])):
            stack.append(i)
        else:
            while(stack[-1] != -1 and heights[i] <= heights[stack[-1]]):
                idx = stack.pop()
                maxArea = max(maxArea, (i-stack[-1]-1) * heights[idx])
            stack.append(i)
    for i in range(1, len(stack)):
        maxArea = max(maxArea, (len(heights)-stack[i-1]-1) * heights[stack[i]])
    return maxArea

### 分治法
def largestRectangleArea(self, heights: List[int]) -> int:
    def helper(start, end):
        if(start > end):
            return 0
        elif(end - start <= 1):
            return max(min(heights[start:end+1]) * (end - start + 1), max(heights[start: end+1]))
        else:
            mid = heights[start: end+1].index(min(heights[start:end+1])) + start
            left = helper(start, mid-1)
            right = helper(mid+1, end)
            return max(heights[mid] * (end - start + 1), left, right)
    if(heights):
        return helper(0, len(heights)-1)
    return 0
