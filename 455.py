import unittest


class Solution:
    def findContentChildren(self, g, s) -> int:
        g.sort()
        s.sort()
        gi = 0
        si = 0
        while gi < len(g) and si < len(s):
            if s[si] >= g[gi]:
                si += 1
                gi += 1
                continue

            si += 1

        return gi


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        g = [1,2,3]
        s = [1,1]
        expected = 1
        actual = self.solution.findContentChildren(g, s)
        self.assertEqual(expected, actual)

    def test_2(self):
        g = [1,2]
        s = [1,2,3]
        expected = 2
        actual = self.solution.findContentChildren(g, s)
        self.assertEqual(expected, actual)

    def test_3(self):
        g = [10, 9, 8, 7]
        s = [5, 6, 7, 8]
        expected = 2
        actual = self.solution.findContentChildren(g, s)
        self.assertEqual(expected, actual)
