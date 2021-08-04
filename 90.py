class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = [[]]
        pre_index = 0
        for i, n in enumerate(nums):
            start_index = len(result)
            if i == 0 or n != nums[i-1]:
                start = 0
            else:
                start = pre_index

            for j in range(start, len(result)):
                tmp = result[j].copy()
                tmp.append(n)
                result.append(tmp)

            pre_index = start_index

        return result