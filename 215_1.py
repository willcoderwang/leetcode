class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return

        t = k - 1
        start = 0
        end = len(nums) - 1
        while True:
            r = self.sort_one(nums, start, end)
            if r == t:
                return nums[t]
            elif r < t:
                start = r + 1
            else:
                end = r - 1

        return nums[t]

    def sort_one(self, nums, start, end):
        if start >= end:
            return start

        s, e = start, end
        while s < e:
            while s < e and nums[s] >= nums[e]:
                e -= 1

            nums[s], nums[e] = nums[e], nums[s]

            while s < e and nums[s] >= nums[e]:
                s += 1

            nums[s], nums[e] = nums[e], nums[s]

        return s
