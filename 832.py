class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        return [self.flipAndInvertList(num_list) for num_list in A]

    def flipAndInvertList(self, alist):
        alist_len = len(alist)
        res = [0] * alist_len

        for i, num in enumerate(alist):
            flip_i = alist_len - 1 - i

            if num == 0:
                res[flip_i] = 1
            elif num == 1:
                res[flip_i] = 0
            else:
                raise ValueError("invalid num in alist")

        return res
