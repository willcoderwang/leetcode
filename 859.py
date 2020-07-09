class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B) or len(A) < 2:
            return False

        diff_count = 0
        diff_index = []
        for i in range(len(A)):
            if A[i] != B[i]:
                diff_count += 1
                diff_index.append(i)
                if diff_count > 2:
                    return False

        if diff_count == 1:
            return False

        elif diff_count == 0:
            if len(set(A)) == len(A):
                return False
            else:
                return True

        elif diff_count == 2:
            if A[diff_index[0]] == B[diff_index[1]] and A[diff_index[1]] == B[diff_index[0]]:
                return True
            else:
                return False

        return False