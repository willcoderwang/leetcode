class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        max_p = prices[-1]
        max_list = [max_p] * len(prices)
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > max_p:
                max_p = prices[i]

            max_list[i] = max_p

        result = 0
        for i in range(len(prices)):
            if max_list[i] - prices[i] > result:
                result = max_list[i] - prices[i]

        return result