class MyStack:

    def __init__(self):
        self.queue = []
        self.helper_queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.helper_queue.append(self.queue.pop(0))
        
        n = self.queue.pop(0)
        self.queue, self.helper_queue = self.helper_queue, self.queue
        return n

    def top(self) -> int:
        while len(self.queue) > 1:
            self.helper_queue.append(self.queue.pop(0))
        
        n = self.queue.pop(0)
        self.helper_queue.append(n)
        self.queue, self.helper_queue = self.helper_queue, self.queue
        return n

    def empty(self) -> bool:
        return len(self.queue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
