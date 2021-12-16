import unittest


class Solution:
    def canJump(self, nums) -> bool:
        current = 0
        furthest = nums[0]

        if furthest >= len(nums) - 1:
            return True

        while current <= furthest:
            if current + nums[current] > furthest:
                furthest = current + nums[current]
                if furthest >= len(nums) - 1:
                    return True
            current += 1

        return False


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        nums = [2,3,1,1,4]
        res = self.solution.canJump(nums)
        self.assertTrue(res)

    def test_2(self):
        nums = [3,2,1,0,4]
        res = self.solution.canJump(nums)
        self.assertFalse(res)