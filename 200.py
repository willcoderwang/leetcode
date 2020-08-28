class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    count += 1
                    self.remove_island(grid, r, c)

        return count

    def remove_island(self, grid, r, c):
        rows = len(grid)
        cols = len(grid[0])
        if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
            return

        grid[r][c] = '0'

        self.remove_island(grid, r - 1, c)
        self.remove_island(grid, r + 1, c)
        self.remove_island(grid, r, c - 1)
        self.remove_island(grid, r, c + 1)
