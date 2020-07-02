class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        hash_list = [0] * 101
        for n in nums:
            hash_list[n] += 1

        sum_list = [0] * 100
        the_sum = 0
        for n in range(100):
            the_sum += hash_list[n]
            sum_list[n] = the_sum

        result = []
        for n in nums:
            if n == 0:
                result.append(0)
            else:
                result.append(sum_list[n - 1])

        return result