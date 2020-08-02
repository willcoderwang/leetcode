class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        last_num = nums[-1]
        pre_nums_sets = self.subsets(nums[:-1])
        addition_sets = []
        for s in pre_nums_sets:
            s_cp = s.copy()
            s_cp.append(last_num)
            addition_sets.append(s_cp)

        result = pre_nums_sets + addition_sets

        return result