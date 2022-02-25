class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(n) for n in version1.split('.')]
        v2 = [int(n) for n in version2.split('.')]

        max_len = max(len(v1), len(v2))

        if len(v1) < max_len:
            v1.extend([0] * (max_len - len(v1)))

        if len(v2) < max_len:
            v2.extend([0] * (max_len - len(v2)))

        for i in range(max_len):
            if v1[i] == v2[i]:
                continue
            if v1[i] < v2[i]:
                return -1
            if v1[i] > v2[i]:
                return 1

        return 0
