class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        the_sum = sum(nums)
        half = the_sum / 2
        part_sum = 0
        for i, n in enumerate(nums):
            part_sum += n
            if part_sum > half:
                return nums[:i+1]