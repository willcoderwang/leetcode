class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        front = 0
        end = len(nums) - 1

        while front < end:
            mid = (front + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                front = mid + 1

        if nums[front] != target:
            return [-1, -1]

        first_index = front
        end = len(nums) - 1
        while front < end:
            mid = (front + end) // 2
            if nums[mid] > target:
                end = mid
            elif nums[mid] < target:
                front = mid + 1
            else:
                if nums[mid + 1] != target:
                    end_index = mid
                    return [first_index, end_index]
                else:
                    front = mid + 1
        end_index = end

        return [first_index, end_index]