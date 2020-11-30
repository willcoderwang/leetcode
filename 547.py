class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        the_map = [x for x in range(len(M))]
        for j in range(1, len(M)):
            for i in range(j):
                if M[i][j]:
                    self._set_circle(the_map, j, i)

        result = 0
        for i in range(len(M)):
            if self._get_circle(the_map, i) == i:
                result += 1

        return result

    def _set_circle(self, the_map, j, i):
        if the_map[j] == j:
            the_map[j] = self._get_circle(the_map, i)
        else:
            x = self._get_circle(the_map, i)
            the_map[x] = the_map[j]

    def _get_circle(self, the_map, i):
        x = i
        while the_map[x] != x:
            x = self._get_circle(the_map, the_map[x])
        return x
