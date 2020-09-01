class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0

        results = [[None for i in range(len(matrix[0]))] for j in range(len(matrix))]

        the_max = 0
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if self.result_at(results, matrix, r, c) > the_max:
                    the_max = self.result_at(results, matrix, r, c)

        return the_max

    def result_at(self, results, matrix, r, c):
        if r < 0 or r >= len(matrix) or c < 0 or c >= len(matrix[0]):
            return 0

        if results[r][c] is not None:
            return results[r][c]

        the_max = 0
        if r-1 >= 0 and matrix[r-1][c] > matrix[r][c]:
            if self.result_at(results, matrix, r-1, c) > the_max:
                the_max = self.result_at(results, matrix, r-1, c)

        if r+1 < len(matrix) and matrix[r+1][c] > matrix[r][c]:
            if self.result_at(results, matrix, r+1, c) > the_max:
                the_max = self.result_at(results, matrix, r+1, c)

        if c-1 >= 0 and matrix[r][c-1] > matrix[r][c]:
            if self.result_at(results, matrix, r, c-1) > the_max:
                the_max = self.result_at(results, matrix, r, c-1)

        if c+1 < len(matrix[0]) and matrix[r][c+1] > matrix[r][c]:
            if self.result_at(results, matrix, r, c+1) > the_max:
                the_max = self.result_at(results, matrix, r, c+1)

        results[r][c] = the_max + 1
        return results[r][c]