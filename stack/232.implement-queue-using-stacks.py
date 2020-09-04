class MyQueue:

    # 栈stack只能后进先出，队列queue只能先进先出
    # 因为python没有栈的数据结构，所以我们用list来模拟栈操作，append操作代表栈顶加入元素，
    # pop操作代表弹出栈顶元素，此外还可以使用len函数计算栈的元素个数，其他的列表操作均不可以使用

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.assist_stack = []
        self.front = None

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        if not self.stack:  # 当stack为空时，此时传入的x就是第一个元素
            self.front = x
        self.stack.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.assist_stack:  # 当assist_stack为空时
            while self.stack:  # 当stack非空时
                self.assist_stack.append(self.stack.pop())  # assist_stack一直吸纳stack pop出来的元素，直到stack变成空的

        result = self.assist_stack.pop()

        # 处理完之后assist_stack要把结果还回去stack
        while self.assist_stack:
            pop_element = self.assist_stack.pop()

            # 因为此时已经是stack的倒序，所以pop的第一个元素就是stack的第一个元素，也就是front
            if not self.stack:
                self.front = pop_element

            self.stack.append(pop_element)

        return result

    def peek(self) -> int:
        """
        Get the front element.
        """

        return self.front

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stack:
            return True
        return False

