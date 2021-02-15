class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        pre_jump_max = -1
        jump_max = nums[0]
        jump_count = 0

        if target == 0:
            return 0

        if jump_max >= target:
            return 1

        while jump_max > pre_jump_max:
            jump_count += 1
            new_max = 0
            for i in range(pre_jump_max + 1, jump_max + 1):
                if i + nums[i] > new_max:
                    new_max = i + nums[i]
                    if new_max >= target:
                        return jump_count + 1

            pre_jump_max = jump_max
            jump_max = new_max
        else:
            return None
ß