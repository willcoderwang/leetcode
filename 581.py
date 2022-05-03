class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        left_max = [nums[0]] * len(nums)
        cur_max = nums[0]
        right_min = [nums[-1]] * len(nums)
        cur_min = nums[-1]

        for i in range(len(nums)):
            tmp_max = max(cur_max, nums[i])
            cur_max = tmp_max
            left_max[i] = tmp_max

            ri = len(nums) - 1 - i
            tmp_min = min(cur_min, nums[ri])
            cur_min = tmp_min
            right_min[ri] = tmp_min

        l, r = None, None
        for i in range(len(nums)):
            if left_max[i] != right_min[i]:
                l = i
                break
        else:
            return 0

        for i in range(len(nums) - 1, -1, -1):
            if left_max[i] != right_min[i]:
                r = i
                break

        return r - l + 1
