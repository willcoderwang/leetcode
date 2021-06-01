import unittest


class Solution:
    def canDistribute(self, nums, quantity) -> bool:
        hash_map = [0] * 1000
        for n in nums:
            hash_map[n-1] += 1

        values = [n for n in hash_map if n > 0]

        return self._canDistributeCore(values, quantity)

    def _canDistributeCore(self, values, quantity):
        max_quantity = max(quantity)
        if max_quantity < 1:
            return True

        if max(values) < max_quantity:
            return False

        for i, v in enumerate(values):
            if v >= max_quantity:
                values[i] -= max_quantity
                quantity_max_index = quantity.index(max_quantity)
                quantity[quantity_max_index] = 0
                if self._canDistributeCore(values, quantity):
                    return True
                else:
                    values[i] += max_quantity
                    quantity[quantity_max_index] = max_quantity
        else:
            return False


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        nums = [1, 2, 3, 4]
        quantity = [2]
        expected = False
        actual = self.solution.canDistribute(nums, quantity)
        self.assertEqual(expected, actual)

    def test_2(self):
        nums = [1,2,3,3]
        quantity = [2]
        expected = True
        actual = self.solution.canDistribute(nums, quantity)
        self.assertEqual(expected, actual)

    def test_3(self):
        nums = [1,1,2,2]
        quantity = [2,2]
        expected = True
        actual = self.solution.canDistribute(nums, quantity)
        self.assertEqual(expected, actual)

    def test_4(self):
        nums = [1,1,2,3]
        quantity = [2,2]
        expected = False
        actual = self.solution.canDistribute(nums, quantity)
        self.assertEqual(expected, actual)

    def test_5(self):
        nums = [1,1,1,1,1]
        quantity = [2,3]
        expected = True
        actual = self.solution.canDistribute(nums, quantity)
        self.assertEqual(expected, actual)

    def test_6(self):
        nums = [1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]
        quantity = [5, 4, 3]
        expected = True
        actual = self.solution.canDistribute(nums, quantity)
        self.assertEqual(expected, actual)

    def test_7(self):
        nums = [154, 533, 533, 533, 154, 154, 533, 154, 154]
        quantity = [3, 2, 2, 2]
        expected = True
        actual = self.solution.canDistribute(nums, quantity)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
