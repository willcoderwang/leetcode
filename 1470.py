class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []

        nums_len = len(nums)
        m = nums_len / n

        for i in range(nums_len):
            index = int(i / m) + int(n * (i % m))
            result.append(nums[index])

        return result