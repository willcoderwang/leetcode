import unittest


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = []
        for c in s:
            if c in ['+', '-', '(', ')', ' ']:
                if num:
                    self.handle(stack, int(''.join(num)))
                num = []
                self.handle(stack, c)
            elif '0' <= c <= '9':
                num.append(c)
        if num:
            self.handle(stack, int(''.join(num)))

        return stack[0]

    def handle(self, stack, c):
        if isinstance(c, int):
            if len(stack) == 0 or stack[-1] == '(':
                stack.append(c)
            else:
                op = stack.pop()
                if stack and isinstance(stack[-1], int):
                    p = stack.pop()
                else:
                    p = 0
                if op == '+':
                    r = p + c
                else:
                    r = p - c
                stack.append(r)
        elif c in ['+', '-', '(']:
            stack.append(c)
        elif c == ')':
            p = stack.pop()
            stack.pop()
            self.handle(stack, p)


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        s = "1 + 1"
        expected = 2
        actual = self.solution.calculate(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = " 2-1 + 2 "
        expected = 3
        actual = self.solution.calculate(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "(1+(4+5+2)-3)+(6+8)"
        expected = 23
        actual = self.solution.calculate(s)
        self.assertEqual(expected, actual)

    def test_4(self):
        s = "123"
        expected = 123
        actual = self.solution.calculate(s)
        self.assertEqual(expected, actual)

    def test_5(self):
        s = "-2+ 1"
        expected = -1
        actual = self.solution.calculate(s)
        self.assertEqual(expected, actual)

    def test_6(self):
        s = "1-(-2)"
        expected = 3
        actual = self.solution.calculate(s)
        self.assertEqual(expected, actual)
