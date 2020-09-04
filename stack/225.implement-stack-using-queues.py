class MyStack:

    # 所谓用队列实现栈，主要是栈只能后进先出，队列只能先进先出，两者恰恰相反，所以其实就是考察如何利用先进先出实现后进先出
    # 这里提供的思路也是构建两个队列
    # 比如队列1进来了push了abc三个元素，如果要pop就会按照abc的顺序，现在就希望pop的时候先pop出c
    # 所以另一个队列的作用就是，把队列1的ab pop到队列2中，然后队列1剩下的c再作为pop的输出，最后再把队列2的元素pop回队列1中

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.assit_stack = []

    def push(self, x):
        """
        Push element x onto stack.
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        """
        if not self.empty():
            self.assit_stack = (self.stack[:-1])

            del self.stack[:-1]
            output = self.stack[-1]

            self.stack.pop()
            self.stack = self.assit_stack

            return output

    def top(self):
        """
        Get the top element.
        """
        if not self.empty():
            return self.stack[-1]

    def empty(self):
        """
        Returns whether the stack is empty.
        """
        if len(self.stack) == 0:
            return True
        else:
            return False

