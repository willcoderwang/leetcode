class Solution:
    def findMin(self, nums: List[int]) -> int:
        head = 0
        tail = len(nums) - 1
        while head < tail:
            mid = (head + tail) // 2
            if nums[head] <= nums[mid] <= nums[tail]:
                return nums[head]
            elif nums[head] <= nums[mid]:
                head = mid + 1
            else:
                tail -= 1

        return nums[head]
