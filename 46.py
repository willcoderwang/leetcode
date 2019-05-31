class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        if len(nums) == 1:
            return [nums]

        result = []

        for index, num in enumerate(nums):
            rest_of_nums = nums.copy()
            del rest_of_nums[index]
            for permutation in self.permute(rest_of_nums):
                permutation.insert(0, num)
                result.append(permutation)

        return result