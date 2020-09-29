class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        for i in range(len(s2)-len(s1)+1):
            if self.permutation_equal(s1, s2[i:i+len(s1)]):
                return True
        else:
            return False

    def permutation_equal(self, s1, s2):
        return sorted(s1) == sorted(s2)
