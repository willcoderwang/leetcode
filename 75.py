class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        p0 = 0
        p2 = len(nums) - 1
        i = 0
        while i <= p2:
            if nums[i] == 0:
                nums[i] = nums[p0]
                nums[p0] = 0
                p0 += 1
                i = max(i, p0)
            elif nums[i] == 2:
                nums[i] = nums[p2]
                nums[p2] = 2
                p2 -= 1
            else:
                i += 1