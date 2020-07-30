class Solution:
    def isValid(self, S: str) -> bool:
        while 'abc' in S:
            start = S.index('abc')
            S = S[:start] + S[start + 3:]

        return S == ''