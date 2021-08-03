import unittest


class Solution:
    def productExceptSelf(self, nums):
        product_left = [1] * len(nums)
        product_right = [1] * len(nums)

        p = 1
        for i in reversed(range(len(nums)-1)):
            p = p * nums[i+1]
            product_right[i] = p

        p = 1
        for i in range(1, len(nums)):
            p = p * nums[i - 1]
            product_left[i] = p

        result = []
        for i in range(len(nums)):
            result.append(product_left[i] * product_right[i])

        return result


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        nums = [1,2,3,4]
        expected = [24,12,8,6]
        actual = self.solution.productExceptSelf(nums)
        self.assertEqual(actual, expected)

    def test_2(self):
        nums = [-1,1,0,-3,3]
        expected = [0,0,9,0,0]
        actual = self.solution.productExceptSelf(nums)
        self.assertEqual(actual, expected)