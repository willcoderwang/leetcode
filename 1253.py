class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        if sum(colsum) != upper + lower:
            return []

        n = len(colsum)
        result = [[0 for i in range(n)] for j in range(2)]

        for i in range(n):
            if colsum[i] == 2:
                result[0][i] = 1
                result[1][i] = 1
                upper -= 1
                lower -= 1

        if upper < 0 or lower < 0:
            return []

        for i in range(n):
            if colsum[i] == 1:
                if upper:
                    result[0][i] = 1
                    upper -= 1
                elif lower:
                    result[1][i] = 1
                    lower -= 1

        return result
