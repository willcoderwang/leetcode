class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        nums_copy = nums.copy()
        first_decr = True
        for i in range(len(nums_copy) - 1):
            if nums_copy[i] > nums_copy[i + 1]:
                if first_decr:
                    first_decr = False

                    # try change nums_copy[i]
                    if i == 0:
                        nums_copy[0] = -10e5
                    elif nums_copy[i - 1] <= nums_copy[i + 1]:
                        nums_copy[i] = nums_copy[i - 1]
                    # cannot change nums_copy[i], change nums_copy[i+1]
                    else:
                        nums_copy[i + 1] = nums_copy[i]
                else:
                    return False

        return True
