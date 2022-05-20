class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[-1][-1] != 0 or obstacleGrid[0][0] != 0:
            return 0

        obstacleGrid[-1][-1] = -1
        for i in range(len(obstacleGrid) - 1, -1, -1):
            for j in range(len(obstacleGrid[i]) - 1, -1, -1):
                if obstacleGrid[i][j] != 0:
                    continue

                res = 0
                if j + 1 < len(obstacleGrid[i]) and obstacleGrid[i][j + 1] < 0:
                    res += obstacleGrid[i][j + 1]
                if i + 1 < len(obstacleGrid) and obstacleGrid[i + 1][j] < 0:
                    res += obstacleGrid[i + 1][j]

                obstacleGrid[i][j] = res

        return -obstacleGrid[0][0]
