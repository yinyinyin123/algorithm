
### one code one day
###2020/05/12
### leetcode 155 最小栈

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.numstack = []
        self.minstack = []


    def push(self, x: int) -> None:
        self.numstack.append(x)
        if(len(self.minstack) == 0):
            self.minstack.append(x)
        else:
            if(self.minstack[-1] >= x):
                self.minstack.append(x)

    def pop(self) -> None:
        if(self.numstack[-1] == self.minstack[-1]):
            self.minstack.pop()
        self.numstack.pop()

    def top(self) -> int:
        return self.numstack[-1]


    def getMin(self) -> int:
        return self.minstack[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
