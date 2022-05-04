class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        res = 0
        p_head = 0
        p_tail = len(nums) - 1
        nums.sort()
        while p_tail > p_head:
            if nums[p_head] + nums[p_tail] == k:
                res += 1
                p_head += 1
                p_tail -= 1
            elif nums[p_head] + nums[p_tail] < k:
                p_head += 1
            else:
                p_tail -= 1

        return res