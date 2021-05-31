import unittest


class Solution:
    def surfaceArea(self, grid) -> int:
        n = len(grid)
        area = 0
        cnt = 0

        for r, row in enumerate(grid):
            for c, col in enumerate(row):
                if col > 0:
                    cnt += 1

                if r - 1 < 0:
                    area += col
                elif col > grid[r-1][c]:
                    area += col - grid[r-1][c]
                if c - 1 < 0:
                    area += col
                elif col > grid[r][c-1]:
                    area += col - grid[r][c-1]
                if r + 1 >= n:
                    area += col
                elif col > grid[r+1][c]:
                    area += col - grid[r+1][c]
                if c + 1 >= n:
                    area += col
                elif col > grid[r][c+1]:
                    area += col - grid[r][c+1]

        area += cnt * 2
        return area


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        grid = [[2]]
        expected = 10
        actual = self.solution.surfaceArea(grid)
        self.assertEqual(expected, actual)

    def test_2(self):
        grid = [[1,2],[3,4]]
        expected = 34
        actual = self.solution.surfaceArea(grid)
        self.assertEqual(expected, actual)

    def test_3(self):
        grid = [[1,0],[0,2]]
        expected = 16
        actual = self.solution.surfaceArea(grid)
        self.assertEqual(expected, actual)

    def test_4(self):
        grid = [[1,1,1],[1,0,1],[1,1,1]]
        expected = 32
        actual = self.solution.surfaceArea(grid)
        self.assertEqual(expected, actual)

    def test_5(self):
        grid = [[2,2,2],[2,1,2],[2,2,2]]
        expected = 46
        actual = self.solution.surfaceArea(grid)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
