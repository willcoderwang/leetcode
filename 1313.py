class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        len_nums = len(nums)
        for i in range(int(len_nums / 2)):
            result.extend([nums[2 * i + 1]] * nums[2 * i])

        return result