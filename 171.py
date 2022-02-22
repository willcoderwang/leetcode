class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        for l in columnTitle:
            res = res * 26 + (ord(l) - 64)

        return res
