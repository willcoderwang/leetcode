class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        count_sum = 0
        start = 0
        for i in range(len(grid)-1, -1, -1):
            count = self.negative_count(grid[i], start)
            if count == 0:
                return count_sum
            else:
                count_sum += count
                start = len(grid[i]) - count

        return count_sum

    def negative_count(self, nums, start=0):
        if not nums or nums[-1] >= 0:
            return 0

        if nums[start] < 0:
            return len(nums) - start

        end = len(nums) - 1

        while start < end:
            mid = (start + end) // 2
            if nums[mid] >= 0:
                start = mid + 1
            else:
                end = mid

        return len(nums) - end
