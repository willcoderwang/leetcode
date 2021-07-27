import unittest


class Solution:
    def minSubArrayLen(self, target: int, nums) -> int:
        if not nums:
            return 0

        start = 0
        sum_n = 0
        for n in range(len(nums)):
            sum_n += nums[n]
            if sum_n >= target:
                break
        else:
            return 0

        if n == 0:
            return n+1

        while start + n < len(nums):
            if sum_n >= target:
                if n == 0:
                    return n+1
                sum_n -= nums[start]
                start += 1
                n -= 1
            else:
                sum_n -= nums[start]
                start += 1
                if start + n < len(nums):
                    sum_n += nums[start+n]

        return n + 2


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        target = 7
        nums = [2,3,1,2,4,3]
        expected = 2
        actual = self.solution.minSubArrayLen(target, nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        target = 4
        nums = [1, 4, 1, 1]
        expected = 1
        actual = self.solution.minSubArrayLen(target, nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        target = 11
        nums = [1,1,1,1,1,1,1,1]
        expected = 0
        actual = self.solution.minSubArrayLen(target, nums)
        self.assertEqual(expected, actual)

    def test_4(self):
        target = 11
        nums = [1,2,3,4,5]
        expected = 3
        actual = self.solution.minSubArrayLen(target, nums)
        self.assertEqual(expected, actual)
