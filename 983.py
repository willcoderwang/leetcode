import unittest


class Solution:
    def mincostTickets(self, days, costs) -> int:
        results = [None] * len(days)
        return self.mincost(days, costs, 0, results)

    def mincost(self, days, costs, current, results):

        if current >= len(days):
            return 0

        buy1 = self.mincost_different_buy(0, days, costs, current, results)
        buy7 = self.mincost_different_buy(1, days, costs, current, results)
        buy30 = self.mincost_different_buy(2, days, costs, current, results)

        min_cost = min([buy1, buy7, buy30])
        results[current] = min_cost
        return min_cost

    def mincost_different_buy(self, buy_index, days, costs, current, results):
        if buy_index == 0:
            buy_days = 1
        elif buy_index == 1:
            buy_days = 7
        else:
            buy_days = 30

        current_day = days[current]
        while current < len(days) and days[current] < current_day + buy_days:
            current += 1

        if current < len(days) and results[current]:
            min_cost = costs[buy_index] + results[current]
        else:
            min_cost = costs[buy_index] + self.mincost(days, costs, current, results)

        return min_cost


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        days = [1, 4, 6, 7, 8, 20]
        costs = [2, 7, 15]
        expected = 11
        actual = self.solution.mincostTickets(days, costs)
        self.assertEqual(expected, actual)

    def test_2(self):
        days = [1,2,3,4,5,6,7,8,9,10,30,31]
        costs = [2,7,15]
        expected = 17
        actual = self.solution.mincostTickets(days, costs)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
