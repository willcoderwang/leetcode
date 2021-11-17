class MyStack:

    def __init__(self):
        self.main = []
        self.back = []

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        if not self.main:
            raise ValueError("stack empty, cannot pop")

        t = None
        while self.main:
            t = self.main[0]
            if len(self.main) > 1:
                self.back.append(t)
            self.main = self.main[1:]

        self.main, self.back = self.back, self.main

        return t

    def top(self) -> int:
        if not self.main:
            return

        t = None
        while self.main:
            t = self.main[0]
            self.back.append(t)
            self.main = self.main[1:]

        self.main, self.back = self.back, self.main
        return t

    def empty(self) -> bool:
        return len(self.main) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()