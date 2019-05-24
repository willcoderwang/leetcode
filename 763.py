class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []

        hash_map = [0] * 26
        for i, c in enumerate(S):
            if i > hash_map[ord(c) - ord('a')]:
                hash_map[ord(c) - ord('a')] = i

        head = 0
        while head < len(S):
            tail = hash_map[ord(S[head]) - ord('a')]
            p = head + 1
            while p < tail:
                if hash_map[ord(S[p]) - ord('a')] > tail:
                    tail = hash_map[ord(S[p]) - ord('a')]

                p += 1

            res.append(tail - head + 1)

            head = tail + 1

        return res