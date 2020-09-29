class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.check_inclusion_core(s1, s2, 0, len(s2)-len(s1))

    def check_inclusion_core(self, s1, s2, start, stop):
        if stop < start:
            return False

        mid = (start + stop) // 2
        if self.permutation_equal(s1, s2[mid: mid+len(s1)]):
            return True

        return self.check_inclusion_core(s1, s2, start, mid-1) or self.check_inclusion_core(s1, s2, mid+1, stop)

    def permutation_equal(self, s1, s2):
        return sorted(s1) == sorted(s2)