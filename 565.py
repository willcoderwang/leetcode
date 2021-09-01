import unittest


class Solution:
    def arrayNesting(self, nums) -> int:
        results = [None] * len(nums)
        max_r = 0

        for i in range(len(nums)):
            if results[i] is not None:
                continue

            cr = 1
            c = i
            while True:
                c = nums[c]
                if results[c] is not None:
                    break

                results[c] = cr
                if cr > max_r:
                    max_r = cr
                cr += 1

        return max_r


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        nums = [5,4,0,3,1,6,2]
        expected = 4
        actual = self.solution.arrayNesting(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [0,1,2]
        expected = 1
        actual = self.solution.arrayNesting(nums)
        self.assertEqual(expected, actual)
