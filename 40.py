class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        return self.combine_sorted(candidates, target)

    def combine_sorted(self, candidates, target):
        if target <= 0:
            return []

        results = []

        for i in range(len(candidates)):
            if i > 0 and candidates[i-1] == candidates[i]:
                continue

            if candidates[i] == target:
                results.append([candidates[i]])
                return results

            if candidates[i] > target:
                break

            sub_results = self.combine_sorted(candidates[i+1:], target - candidates[i])

            if not sub_results:
                continue

            for sub_result in sub_results:
                result = [candidates[i]]
                result.extend(sub_result)
                results.append(result)

        return results