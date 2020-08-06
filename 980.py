class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        count0 = 0
        index_1 = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    count0 += 1
                elif grid[i][j] == 1:
                    index_1 = (i, j)

        return self._move_to(grid, index_1[0] + 1, index_1[1], count0) + \
               self._move_to(grid, index_1[0] - 1, index_1[1], count0) + \
               self._move_to(grid, index_1[0], index_1[1] + 1, count0) + \
               self._move_to(grid, index_1[0], index_1[1] - 1, count0)

    def _move_to(self, grid, i, j, count):
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return 0

        if grid[i][j] == -1:
            return 0

        elif grid[i][j] == 2:
            if count == 0:
                return 1
            else:
                return 0

        elif grid[i][j] == 0:
            temp = grid[i][j]
            grid[i][j] = -1
            result = self._move_to(grid, i+1, j, count-1) + self._move_to(grid, i-1, j, count-1) + \
                self._move_to(grid, i, j+1, count-1) + self._move_to(grid, i, j-1, count-1)
            grid[i][j] = temp
            return result

        return 0
