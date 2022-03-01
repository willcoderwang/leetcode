class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count, smaller_count = 0, 0
        for n in nums:
            if n == target:
                count += 1
            elif n < target:
                smaller_count += 1

        if count < 1:
            return []

        return [smaller_count + i for i in range(count)]
