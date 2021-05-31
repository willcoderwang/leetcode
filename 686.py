import unittest


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        for i, ac in enumerate(a):
            if ac == b[0]:
                ai = i
                cnt = 1
                for bi, bc in enumerate(b):
                    if ai >= len(a):
                        ai = ai % len(a)
                        cnt += 1

                    if bc != a[ai]:
                        break

                    ai += 1
                else:
                    return cnt

        return -1


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        a = "abcd"
        b = "cdabcdab"
        expected = 3
        actual = self.solution.repeatedStringMatch(a, b)
        self.assertEqual(expected, actual)

    def test_2(self):
        a = "a"
        b = "aa"
        expected = 2
        actual = self.solution.repeatedStringMatch(a, b)
        self.assertEqual(expected, actual)

    def test_3(self):
        a = "a"
        b = "a"
        expected = 1
        actual = self.solution.repeatedStringMatch(a, b)
        self.assertEqual(expected, actual)

    def test_4(self):
        a = "abc"
        b = "wxyz"
        expected = 1
        actual = self.solution.repeatedStringMatch(a, b)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
