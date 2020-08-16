class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 1:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 2

        the_map = [-1] * n
        the_map[0] = 1
        the_map[1] = 2

        for i in range(2, n):
            the_map[i] = the_map[i-1] + the_map[i-2]

        return the_map[n-1]
