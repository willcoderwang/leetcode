class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if nums[0] > nums[1]:
            max_1, max_2 = nums[:2]
        else:
            max_2, max_1 = nums[:2]

        for n in nums[2:]:
            if n > max_1:
                max_1, max_2 = n, max_1
            elif n > max_2:
                max_2 = n

        return (max_1 - 1) * (max_2 - 1)