import math


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]  # 辅助栈，每次有元素入栈时，辅助栈也入栈，但是辅助站入的是所有元素的最小值

    def push(self, x: int) -> None:
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))  # 入的是所有元素的最小值，所以也要考虑新入栈的元素会不会最小

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]  # top返回的是正常栈的栈顶元素

    def getMin(self) -> int:
        return self.min_stack[-1]  # getmin是为了返回最小值，直接返回辅助栈就行

