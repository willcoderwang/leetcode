class Solution:
    def findLucky(self, arr: List[int]) -> int:
        the_hash = [0] * 500
        for i in arr:
            the_hash[i - 1] += 1

        for i in range(len(the_hash) - 1, -1, -1):
            if i + 1 == the_hash[i]:
                return i + 1

        return -1