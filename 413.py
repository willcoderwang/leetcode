class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        result = 0
        diff = None
        count = 0

        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == diff:
                count += 1
            else:
                diff = nums[i + 1] - nums[i]
                if count >= 2:
                    result += int(count * (count - 1) / 2)

                count = 1

        if count >= 2:
            result += int(count * (count - 1) / 2)

        return result
