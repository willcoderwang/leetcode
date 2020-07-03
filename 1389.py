class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        final_index = self.get_final_index(index)
        result = [0] * len(nums)
        for i in range(len(nums)):
            result[final_index[i]] = nums[i]

        return result

    def get_final_index(self, index):
        final_index = index.copy()
        index_len = len(index)
        if index_len < 2:
            return index

        for i in range(index_len):
            for j in range(i+1, index_len):
                if final_index[i] >= index[j]:
                    final_index[i] += 1

        return final_index