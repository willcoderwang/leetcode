class Solution:
    def oddCells(self, n: int, m: int, indices: List[List[int]]) -> int:
        ns = [0] * n
        ms = [0] * m

        for index in indices:
            ns[index[0]] = 0 if ns[index[0]] else 1
            ms[index[1]] = 0 if ms[index[1]] else 1

        return sum(ns) * (m - sum(ms)) + (n - sum(ns)) * sum(ms)
