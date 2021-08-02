import unittest


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1

        the_max = 0
        nums = [0, 1]
        for i in range(2, n+1):
            if i % 2 == 0:
                tmp = nums[i//2]
            else:
                tmp = nums[i // 2] + nums[i // 2 + 1]

            nums.append(tmp)

            if tmp > the_max:
                the_max = tmp

        return the_max


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        n = 7
        expected = 3
        actual = self.solution.getMaximumGenerated(n)
        self.assertEqual(actual, expected)

    def test_2(self):
        n = 2
        expected = 1
        actual = self.solution.getMaximumGenerated(n)
        self.assertEqual(actual, expected)

    def test_3(self):
        n = 3
        expected = 2
        actual = self.solution.getMaximumGenerated(n)
        self.assertEqual(actual, expected)


