class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(1, len(s)//2 + 1):
            if len(s) % i != 0:
                continue

            times = len(s) // i
            if times < 2:
                continue

            if s[:i] * times == s:
                return True

        return False