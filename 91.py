import unittest


class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0

        for i, c in enumerate(s):
            if c == '0':
                if i == 0:
                    return 0
                elif i != 0 and s[i-1] > '3':
                    return 0

        num_2 = 0
        num_1 = 0 if s[-1] == '0' else 1

        for i in reversed(range(0, len(s)-1)):
            result = 0
            if s[i] != '0':
                result += num_1
            if s[i] != '0' and int(s[i:i+2]) <= 26:
                result += num_2 if s[i+2:] else 1

            num_2 = num_1
            num_1 = result

        return num_1


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        s = "12"
        expected = 2
        actual = self.solution.numDecodings(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "226"
        expected = 3
        actual = self.solution.numDecodings(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "0"
        expected = 0
        actual = self.solution.numDecodings(s)
        self.assertEqual(expected, actual)

    def test_4(self):
        s = "06"
        expected = 0
        actual = self.solution.numDecodings(s)
        self.assertEqual(expected, actual)

    def test_5(self):
        s = "2101"
        expected = 1
        actual = self.solution.numDecodings(s)
        self.assertEqual(expected, actual)

    def test_6(self):
        s = "10"
        expected = 1
        actual = self.solution.numDecodings(s)
        self.assertEqual(expected, actual)

