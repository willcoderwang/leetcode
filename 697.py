class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0

        the_hash = [[None, None, 0] for i in range(50000)]
        for i, n in enumerate(nums):
            if the_hash[n][0] is None:
                the_hash[n] = [i, i, 1]
            else:
                the_hash[n][1] = i
                the_hash[n][2] += 1

        max_count = 1
        length = 1
        for i in the_hash:
            if i[2] > max_count or (i[2] == max_count and i[1] - i[0] + 1 < length):
                max_count = i[2]
                length = i[1] - i[0] + 1

        return length
