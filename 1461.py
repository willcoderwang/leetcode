import unittest


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        target = pow(2, k)
        count = 0
        hash = [False] * target
        for i in range(len(s) - k + 1):
            idx = int(s[i:i+k], 2)
            if not hash[idx]:
                hash[idx] = True
                count += 1
                if count == target:
                    return True

        return False


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        s = "00110110"
        k = 2
        actual = self.solution.hasAllCodes(s, k)
        self.assertTrue(actual)

    def test_2(self):
        s = "00110"
        k = 2
        actual = self.solution.hasAllCodes(s, k)
        self.assertTrue(actual)

    def test_3(self):
        s = "0110"
        k = 1
        actual = self.solution.hasAllCodes(s, k)
        self.assertTrue(actual)

    def test_4(self):
        s = "0110"
        k = 2
        actual = self.solution.hasAllCodes(s, k)
        self.assertFalse(actual)

    def test_5(self):
        s = "0000000001011100"
        k = 4
        actual = self.solution.hasAllCodes(s, k)
        self.assertFalse(actual)
