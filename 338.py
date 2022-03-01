class Solution:
    def countBits(self, n: int) -> List[int]:
        results = [0]
        if n == 0:
            return results

        end = 0
        count = 0

        while True:
            p = 0
            while p <= end:
                results.append(results[p] + 1)
                count += 1
                if count == n:
                    return results
                p += 1
            end = len(results) - 1
