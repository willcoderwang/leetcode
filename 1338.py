class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        the_map = [0] * 100000
        for i in arr:
            the_map[i - 1] += 1

        the_map.sort(reverse=True)
        count = 0
        removed = 0
        while removed < len(arr) / 2:
            count += 1
            removed += the_map[count - 1]

        return count