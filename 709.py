class Solution:
    def toLowerCase(self, s: str) -> str:
        result_s = []
        for c in s:
            if 65 <= ord(c) <= 90:
                result_s.append(chr(ord(c) + 32))
            else:
                result_s.append(c)

        return ''.join(result_s)