class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target == 0:
            return [[]]

        if not candidates:
            return []

        results = []
        for index, c in enumerate(candidates):
            if c > target:
                continue
            elif c == target:
                results.append([c])
            else:
                rest_candidates = candidates[index+1:]

                for i in range(1, target // c + 1):

                    rest_results = self.combinationSum(rest_candidates, target - i * c)

                    for rr in rest_results:
                        rr.extend([c] * i)
                        results.append(rr)

        return results