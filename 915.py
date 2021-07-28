import unittest


class Solution:
    def partitionDisjoint(self, nums) -> int:
        min_of_right = [None] * len(nums)
        min_tmp = nums[-1]
        for i in reversed(range(len(nums))):
            if min_tmp > nums[i]:
                min_tmp = nums[i]
            min_of_right[i] = min_tmp

        max_tmp = nums[0]
        for i in range(1, len(nums)):
            if min_of_right[i] >= max_tmp:
                return i

            if max_tmp < nums[i]:
                max_tmp = nums[i]


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        nums = [5,0,3,8,6]
        expected = 3
        actual = self.solution.partitionDisjoint(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1,1,1,0,6,12]
        expected = 4
        actual = self.solution.partitionDisjoint(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [1,1]
        expected = 1
        actual = self.solution.partitionDisjoint(nums)
        self.assertEqual(expected, actual)
