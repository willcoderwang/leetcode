class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        the_map = [False] * (len(nums) + 1)
        for n in nums:
            the_map[n] = True

        for n in range(len(the_map)):
            if not the_map[n]:
                return n

        return
