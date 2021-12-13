import unittest


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        for i in range(k):
            if len(num) <= 1:
                return '0'

            for j in range(len(num)-1):
                if num[j] > num[j+1]:
                    bigger_i = j
                    break
            else:
                bigger_i = j+1

            num = num[:bigger_i] + num[bigger_i+1:]

            while num and num[0] == '0':
                num = num[1:]

            if not num:
                return '0'

        return num


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        num = "1432219"
        k = 3
        expected = "1219"
        actual = self.solution.removeKdigits(num, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        num = "10200"
        k = 1
        expected = "200"
        actual = self.solution.removeKdigits(num, k)
        self.assertEqual(expected, actual)

    def test_3(self):
        num = "10"
        k = 2
        expected = "0"
        actual = self.solution.removeKdigits(num, k)
        self.assertEqual(expected, actual)

    def test_4(self):
        num = "112"
        k = 1
        expected = "11"
        actual = self.solution.removeKdigits(num, k)
        self.assertEqual(expected, actual)

    def test_4(self):
        num = "9"
        k = 1
        expected = "0"
        actual = self.solution.removeKdigits(num, k)
        self.assertEqual(expected, actual)
