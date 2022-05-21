class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res_map = [None] * (amount + 1)
        res_map[0] = 0

        for amt in range(1, amount + 1):
            res_amt = -1
            for coin in coins:
                if coin == amt:
                    res_amt = 1
                    break
                elif coin > amt:
                    continue
                else:
                    if res_map[amt - coin] > 0 and (res_map[amt - coin] + 1 < res_amt or res_amt < 0):
                        res_amt = res_map[amt - coin] + 1

            res_map[amt] = res_amt

        return res_map[amount]
