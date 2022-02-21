class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        results = []

        def bt(result, n):
            result.append(n)

            if n == target:
                result_cp = result.copy()
                results.append(result_cp)
                result.pop()
                return

            for m in graph[n]:
                bt(result, m)

            result.pop()

        bt([], 0)
        return results
