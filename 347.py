class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        the_dict = dict()
        for num in nums:
            the_dict[num] = the_dict.get(num, 0) + 1

        sort_orders = sorted(the_dict.items(), key=lambda x: x[1], reverse=True)
        return [i[0] for i in sort_orders[:k]]