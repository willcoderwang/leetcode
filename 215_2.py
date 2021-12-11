import heapq
import unittest


class Solution:
    def findKthLargest(self, nums, k: int) -> int:
        h = []
        for n in nums:
            if len(h) < k:
                heapq.heappush(h, n)
            elif n > h[0]:
                heapq.heapreplace(h, n)

        return h[0]


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        nums = [3,2,1,5,6,4]
        k = 2
        expected = 5
        actual = self.solution.findKthLargest(nums, k)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [3,2,3,1,2,4,5,5,6]
        k = 4
        expected = 4
        actual = self.solution.findKthLargest(nums, k)
        self.assertEqual(expected, actual)
