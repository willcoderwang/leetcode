class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        probability = [0] * n
        probability[end] = 1

        while True:
            updated = False
            for i, e in enumerate(edges):
                first_node, second_node = e
                if probability[first_node] < probability[second_node] * succProb[i]:
                    probability[first_node] = probability[second_node] * succProb[i]
                    updated = True

                if probability[second_node] < probability[first_node] * succProb[i]:
                    probability[second_node] = probability[first_node] * succProb[i]
                    updated = True

            if not updated:
                break

        return probability[start]