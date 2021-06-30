import unittest


class Solution:
    def search(self, nums, target) -> bool:
        return self.search_core(nums, target, 0, len(nums)-1)

    def search_core(self, nums, target, start, end):
        if start > end:
            return False

        mid = (start + end) // 2
        if nums[mid] == target:
            return True

        if nums[mid] < target:
            if nums[start] < nums[mid]:
                return self.search_core(nums, target, mid+1, end)
            else:
                return self.search_core(nums, target, start, mid-1) or self.search_core(nums, target, mid+1, end)
        else:
            if nums[start] <= nums[mid]:
                return self.search_core(nums, target, start, mid-1) or self.search_core(nums, target, mid+1, end)
            else:
                return self.search_core(nums, target, start, mid-1)


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        nums = [2,5,6,0,0,1,2]
        target = 0
        actual = self.solution.search(nums, target)
        self.assertTrue(actual)

    def test_2(self):
        nums = [2,5,6,0,0,1,2]
        target = 3
        actual = self.solution.search(nums, target)
        self.assertFalse(actual)

    def test_3(self):
        nums = [1, 0, 1, 1, 1]
        target = 0
        actual = self.solution.search(nums, target)
        self.assertTrue(actual)


if __name__ == '__main__':
    unittest.main()
