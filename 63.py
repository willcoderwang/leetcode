import unittest


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        if obstacleGrid[rows - 1][cols - 1] == 1:
            return 0

        arr = [[None for i in range(cols)] for j in range(rows)]
        for r in range(rows):
            for c in range(cols):
                if obstacleGrid[r][c] == 1:
                    arr[r][c] = 0

        arr[rows-1][cols-1] = 1

        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if arr[r][c] is None:
                    tmp = 0
                    if r + 1 < rows:
                        tmp += arr[r+1][c]
                    if c + 1 < cols:
                        tmp += arr[r][c+1]

                    arr[r][c] = tmp

        return arr[0][0]


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
        expected = 2
        actual = self.solution.uniquePathsWithObstacles(obstacleGrid)
        self.assertEqual(expected, actual)

    def test_2(self):
        obstacleGrid = [[0,1],[0,0]]
        expected = 1
        actual = self.solution.uniquePathsWithObstacles(obstacleGrid)
        self.assertEqual(expected, actual)

    def test_3(self):
        obstacleGrid = [[0,0],[0,1]]
        expected = 0
        actual = self.solution.uniquePathsWithObstacles(obstacleGrid)
        self.assertEqual(expected, actual)

    def test_4(self):
        obstacleGrid = [[0, 0]]
        expected = 1
        actual = self.solution.uniquePathsWithObstacles(obstacleGrid)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
