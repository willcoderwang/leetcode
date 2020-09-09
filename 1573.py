class Solution:
    def numWays(self, s: str) -> int:
        the_map = []
        for i, c in enumerate(s):
            if c == '1':
                the_map.append(i)

        count = len(the_map)
        if count % 3 != 0:
            return 0

        if count == 0:
            if len(s) < 3:
                return 0
            else:
                return int((len(s) - 1) * (len(s) - 2) / 2) % (10 ** 9 + 7)

        unit = int(count / 3)
        return (the_map[unit] - the_map[unit - 1]) * (the_map[unit * 2] - the_map[unit * 2 - 1]) % (10 ** 9 + 7)