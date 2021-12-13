import unittest


class Solution:
    def wiggleMaxLength(self, nums) -> int:
        if len(nums) == 1:
            return 1

        up = None
        changes = 0
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1] and (up is None or up):
                changes += 1
                up = False
            elif nums[i] < nums[i-1] and (up is None or not up):
                changes += 1
                up = True

        return changes + 1




class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        nums = [1,7,4,9,2,5]
        expected = 6
        actual = self.solution.wiggleMaxLength(nums)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1,17,5,10,13,15,10,5,16,8]
        expected = 7
        actual = self.solution.wiggleMaxLength(nums)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [1,2,3,4,5,6,7,8,9]
        expected = 2
        actual = self.solution.wiggleMaxLength(nums)
        self.assertEqual(expected, actual)
