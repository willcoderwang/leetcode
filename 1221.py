class Solution:
    def balancedStringSplit(self, s: str) -> int:
        stack = []
        count = 0
        for c in s:
            if c not in ['L', 'R']:
                continue

            if not stack or stack[len(stack) - 1] == c:
                stack.append(c)
            else:
                stack.pop()
                if not stack:
                    count += 1

        return count