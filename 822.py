import unittest


class Solution:
    def flipgame(self, fronts, backs) -> int:
        hash_map = [None] * 2000
        for i in range(len(fronts)):
            if fronts[i] == backs[i]:
                hash_map[fronts[i] - 1] = False
                continue

            if hash_map[fronts[i]-1] is None:
                hash_map[fronts[i]-1] = True
            if hash_map[backs[i]-1] is None:
                hash_map[backs[i]-1] = True

        for i in range(len(hash_map)):
            if hash_map[i]:
                return i+1
        else:
            return 0


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        fronts = [1,2,4,4,7]
        backs = [1,3,4,1,3]
        expected = 2
        actual = self.solution.flipgame(fronts, backs)
        self.assertEqual(expected, actual)

    def test_1(self):
        fronts = [1]
        backs = [1]
        expected = 0
        actual = self.solution.flipgame(fronts, backs)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
