class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0

        the_map = [False] * len(s)
        the_stack = []

        for i, c in enumerate(s):
            if c == '(':
                the_stack.append(i)
            elif c == ')':
                if len(the_stack) > 0:
                    the_map[i] = True
                    j = the_stack.pop()
                    the_map[j] = True

        result = 0
        tmp_result = 0
        for i in the_map:
            if i:
                tmp_result += 1
            else:
                if tmp_result > result:
                    result = tmp_result
                tmp_result = 0

        return max(result, tmp_result)
