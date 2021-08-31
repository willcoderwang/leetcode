class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        r_2, r_1 = 0, 1
        for i in range(1, n):
            r = r_2 + r_1
            r_2, r_1 = r_1, r

        return r
