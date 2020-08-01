class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        the_hash = [[0 for i in range(len(A))] for j in range(26)]
        for i, word in enumerate(A):
            for j, c in enumerate(word):
                the_hash[ord(c)-97][i] += 1

        res = []

        for index, c in enumerate(the_hash):
            count = 101
            for n in c:
                if n < 1:
                    break
                if n < count:
                    count = n
            else:
                res.extend([chr(97+index)] * count)

        return res