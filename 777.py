import unittest


class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        
        start_l_count = 0
        start_r_count = 0
        end_l_count = 0
        end_r_count = 0
        start_rl = []
        end_rl = []
        
        for i in range(len(start)):
            if start[i] == 'L':
                start_l_count += 1
            elif start[i] == 'R':
                start_r_count += 1
                
            if end[i] == 'L':
                end_l_count += 1
            elif end[i] == 'R':
                end_r_count += 1

            if start[i] != 'X':
                start_rl.append((start[i], i))
            if end[i] != 'X':
                end_rl.append((end[i], i))

        if start_l_count != end_l_count or start_r_count != end_r_count:
            return False

        for i in range(len(start_rl)):
            if start_rl[i][0] != end_rl[i][0]:
                return False

            if start_rl[i][0] == 'L' and start_rl[i][1] < end_rl[i][1]:
                return False

            if start_rl[i][0] == 'R' and start_rl[i][1] > end_rl[i][1]:
                return False

        return True


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        start = "RXXLRXRXL"
        end = "XRLXXRRLX"
        actual = self.solution.canTransform(start, end)
        self.assertTrue(actual)

    def test_2(self):
        start = "X"
        end = "L"
        actual = self.solution.canTransform(start, end)
        self.assertFalse(actual)

    def test_3(self):
        start = "LLR"
        end = "RRL"
        actual = self.solution.canTransform(start, end)
        self.assertFalse(actual)

    def test_4(self):
        start = "XL"
        end = "LX"
        actual = self.solution.canTransform(start, end)
        self.assertTrue(actual)

    def test_4(self):
        start = "XLLR"
        end = "LXLX"
        actual = self.solution.canTransform(start, end)
        self.assertFalse(actual)

    def test_5(self):
        start = "LXXLXRLXXL"
        end = "XLLXRXLXLX"
        actual = self.solution.canTransform(start, end)
        self.assertFalse(actual)




