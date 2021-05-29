import unittest


class Solution:
    def minDeletions(self, s: str) -> int:
        if not s:
            return 0

        hash_map = [0] * 26

        for c in s:
            hash_map[ord(c) - 97] += 1

        frequencies = [f for f in hash_map if f != 0]
        frequencies.sort(reverse=True)

        diff = 0
        next_max = frequencies[0]

        for f in frequencies[1:]:
            if next_max == 1:
                diff += f
            elif f >= next_max:
                next_max -= 1
                diff += f - next_max
            else:
                next_max = min(next_max-1, f)

        return diff


class SolutionTestCase(unittest.TestCase):
    client = Solution()

    def test_1(self):
        s = "aab"
        expected = 0
        actual = self.client.minDeletions(s)
        self.assertEqual(expected, actual)

    def test_2(self):
        s = "aaabbbcc"
        expected = 2
        actual = self.client.minDeletions(s)
        self.assertEqual(expected, actual)

    def test_3(self):
        s = "ceabaacb"
        expected = 2
        actual = self.client.minDeletions(s)
        self.assertEqual(expected, actual)

    def test_4(self):
        s ="accdcdadddbaadbc"
        expected = 1
        actual = self.client.minDeletions(s)
        self.assertEqual(expected, actual)

    def test_5(self):
        s ="abcabc"
        expected = 3
        actual = self.client.minDeletions(s)
        self.assertEqual(expected, actual)

    def test_6(self):
        s ="adec"
        expected = 3
        actual = self.client.minDeletions(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
