class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        cache = [[None for n in range(61)] for k in range(10)]
        return self.core(k, n, cache)

    def core(self, k, n, cache):
        if cache[k][n] is not None:
            return cache[k][n]

        if k == 1:
            if n < 1 or n > 9:
                return []
            else:
                return [[n]]

        results = []
        for i in range(1, 10):
            sub_results = self.core(k - 1, n - i, cache)
            for sub_result in sub_results:
                if i > sub_result[-1]:
                    results.append(sub_result[:] + [i])

        cache[k][n] = results
        return results
