class Solution:
    def originalDigits(self, s: str) -> str:
        count_map = [0] * 26
        for c in s:
            count_map[ord(c) - 97] += 1

        result_map = [0] * 10
        # order matters
        l = [
            (0, 'zero', 'z'),
            (2, 'two', 'w'),
            (4, 'four', 'u'),
            (6, 'six', 'x'),
            (8, 'eight', 'g'),
            (1, 'one', 'o'),
            (3, 'three', 'h'),
            (5, 'five', 'f'),
            (7, 'seven', 's'),
            (9, 'nine', 'i'),
        ]

        for i in l:
            num, num_str, c = i
            self.extract(count_map, result_map, num, num_str, c)

        result_list = []
        for i in range(len(result_map)):
            result_list.extend([chr(48 + i)] * result_map[i])

        return ''.join(result_list)

    def extract(self, count_map, result_map, num, num_str, c):
        n = count_map[ord(c) - 97]
        result_map[num] = n
        self.remove(count_map, num_str, repeat=n)

    def remove(self, count_map, num_str, repeat=1):
        for c in num_str:
            count_map[ord(c) - 97] -= repeat
