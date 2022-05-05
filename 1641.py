class Solution:
    def countVowelStrings(self, n: int) -> int:
        res = [1, 1, 1, 1, 1]
        for i in range(n - 1):
            for j in range(1, 5):
                res[j] += res[j - 1]

        return sum(res)
