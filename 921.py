class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        res = 0
        left_count = 0
        for c in S:
            if c == '(':
                left_count += 1
            elif c == ')':
                if left_count == 0:
                    res += 1
                else:
                    left_count -= 1

        return res + left_count