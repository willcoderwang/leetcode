class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = (nums[0] - 1) * (nums[1] - 1)
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                value = (nums[i] - 1) * (nums[j] - 1)
                if value > result:
                    result = value

        return result
