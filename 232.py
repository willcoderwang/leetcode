class MyQueue:

    def __init__(self):
        self._front = []
        self._data = []

    def push(self, x: int) -> None:
        self._front.append(x)

    def pop(self) -> int:
        if self.empty():
            raise ValueError("queue empty, cannot pop")

        if not self._data:
            while self._front:
                t = self._front.pop()
                self._data.append(t)

        return self._data.pop()

    def peek(self) -> int:
        if not self._data:
            while self._front:
                t = self._front.pop()
                self._data.append(t)

        return self._data[-1]

    def empty(self) -> bool:
        return len(self._front) == 0 and len(self._data) == 0

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()