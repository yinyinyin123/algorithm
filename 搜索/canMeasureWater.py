
### one code one day
### 2020/03/21
### leetcode 365 水壶问题

### 深度优先搜索 栈实现 如果用递归会超过最大递归次数
def canMeasureWater(self, x: int, y: int, z: int) -> bool:
    stack = [(0, 0)]
    self.seen = set()
    while stack:
        remain_x, remain_y = stack.pop()
        if remain_x == z or remain_y == z or remain_x + remain_y == z:
            return True
        if (remain_x, remain_y) in self.seen:
            continue
        self.seen.add((remain_x, remain_y))
        # 把 X 壶灌满。
        stack.append((x, remain_y))
        # 把 Y 壶灌满。
        stack.append((remain_x, y))
        # 把 X 壶倒空。
        stack.append((0, remain_y))
        # 把 Y 壶倒空。
        stack.append((remain_x, 0))
        # 把 X 壶的水灌进 Y 壶，直至灌满或倒空。
        stack.append((remain_x - min(remain_x, y - remain_y), remain_y + min(remain_x, y - remain_y)))
        # 把 Y 壶的水灌进 X 壶，直至灌满或倒空。
        stack.append((remain_x + min(remain_y, x - remain_x), remain_y - min(remain_y, x - remain_x)))
    return False
