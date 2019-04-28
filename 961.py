class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        unique_list = []
        for num in A:
            if num not in unique_list:
                unique_list.append(num)
            else:
                return num
        else:
            return -1
