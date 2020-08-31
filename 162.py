class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        front = 0
        end = len(nums) - 1

        while front < end:
            mid = (front + end) // 2
            if (mid - 1 < 0 or nums[mid - 1] < nums[mid]) and (mid + 1 > len(nums) - 1 or nums[mid + 1] < nums[mid]):
                return mid

            if mid + 1 < len(nums) and nums[mid + 1] > nums[mid]:
                front = mid + 1
            else:
                end = mid

        return end
