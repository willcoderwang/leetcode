class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if s == '()':
            return 1

        lc, rc = 0, 0
        parts = []
        part_start = 0
        for i, c in enumerate(s):
            if c == '(':
                lc += 1
            else:
                rc += 1

            if lc == rc:
                parts.append([part_start, i])
                part_start = i + 1

        if len(parts) == 1:
            return 2 * self.scoreOfParentheses(s[1:-1])

        else:
            res = 0
            for part in parts:
                res += self.scoreOfParentheses(s[part[0]:part[1] + 1])

            return res
