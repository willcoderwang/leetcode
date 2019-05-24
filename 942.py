class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        res = [0]
        d_count = 0
        i_count = 0
        for c in S:
            if c == 'I':
                i_count += 1
                res.append(i_count)
            elif c == 'D':
                d_count += 1
                res.append(-d_count)

        return [x+d_count for x in res]