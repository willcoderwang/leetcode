import unittest


class Solution:
    def canReorderDoubled(self, arr) -> bool:
        l1 = []
        l2 = []
        number_of_zero = 0

        for n in arr:
            if n > 0:
                l1.append(n)
            elif n == 0:
                number_of_zero += 1
            else:
                l2.append(-n)

        if number_of_zero % 2 != 0 or len(l1) % 2 != 0 or len(l2) % 2 != 0:
            return False

        l1_r = self.canReorderDoubledGreat0(l1)
        l2_r = self.canReorderDoubledGreat0(l2)
        return l1_r and l2_r

    def canReorderDoubledGreat0(self, arr):
        if not arr:
            return True

        flag = [True] * len(arr)
        arr.sort()
        p2 = 0
        for p1 in range(len(arr)):
            if not flag[p1]:
                continue

            p2 += 1
            if p2 <= p1:
                p2 = p1 + 1
            while p2 <= len(arr) - 1 and arr[p2] < arr[p1] * 2:
                p2 += 1

            if p2 >= len(arr) or arr[p2] != arr[p1] * 2:
                return False

            flag[p2] = False
        else:
            return True


class SolutionTest(unittest.TestCase):
    solution = Solution()

    def test_1(self):
        arr = [3,1,3,6]
        expected = False
        actual = self.solution.canReorderDoubled(arr)
        self.assertEqual(expected, actual)

    def test_2(self):
        arr = [2,1,2,6]
        expected = False
        actual = self.solution.canReorderDoubled(arr)
        self.assertEqual(expected, actual)

    def test_3(self):
        arr = [4,-2,2,-4]
        expected = True
        actual = self.solution.canReorderDoubled(arr)
        self.assertEqual(expected, actual)

    def test_4(self):
        arr = [1,2,4,16,8,4]
        expected = False
        actual = self.solution.canReorderDoubled(arr)
        self.assertEqual(expected, actual)

    def test_5(self):
        arr = [2,1,2,1,1,1,2,2]
        expected = True
        actual = self.solution.canReorderDoubled(arr)
        self.assertEqual(expected, actual)

    def test_5(self):
        arr = [1,2,1,-8,8,-4,4,-4,2,-2]
        expected = True
        actual = self.solution.canReorderDoubled(arr)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
