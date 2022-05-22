class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        for i in range(len(s)):
            front, end = i, i
            while front >= 0 and end < len(s):
                if s[front] == s[end]:
                    result += 1
                else:
                    break

                front -= 1
                end += 1

            front, end = i, i + 1
            while front >= 0 and end < len(s):
                if s[front] == s[end]:
                    result += 1
                else:
                    break

                front -= 1
                end += 1

        return result
