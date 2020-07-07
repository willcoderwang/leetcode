class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = []
        for c in s:
            if c == '#':
                c2 = result.pop()
                c1 = result.pop()
                result.append(self._two_char_trans(c1, c2))
            else:
                result.append(self._single_digit_trans(c))

        return ''.join(result)

    def _single_digit_trans(self, c):
        if '1' <= c <= '9':
            return chr(ord(c) + 48)

        return c

    def _two_char_trans(self, c1, c2):
        result_num = 0

        if c1 == 'a':
            result_num = 106
        elif c1 == 'b':
            result_num = 116

        if c2 != '0':
            result_num += ord(c2) - 96

        return chr(result_num)
