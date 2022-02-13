class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        results = []

        def generate(result, nleft, nright):
            if nleft >= n:
                result.extend([')'] * (nleft - nright))
                results.append(''.join(result))
                return

            if nleft > nright:
                result_cp = result.copy()
                result_cp.append(')')
                generate(result_cp, nleft, nright+1)

            result.append('(')
            generate(result, nleft+1, nright)

        generate([], 0, 0)

        return results