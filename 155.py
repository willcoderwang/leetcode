class MinStack:

    def __init__(self):
        self._data = []
        self._min = []

    def push(self, val: int) -> None:
        self._data.append(val)
        if not self._min or val <= self._min[-1]:
            self._min.append(val)

    def pop(self) -> None:
        if not self._data:
            raise Exception("stack empty, cannot pop")

        if self._min and self._min[-1] == self._data[-1]:
            self._min.pop()

        self._data.pop()

    def top(self) -> int:
        if not self._data:
            return None

        return self._data[-1]

    def getMin(self) -> int:
        if not self._data:
            return None

        return self._min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
