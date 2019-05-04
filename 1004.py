class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        for index, num in enumerate(A):
            tail = index
            if num == 0:
                if K > 0:
                    K -= 1
                else:
                    break
        else:
            return len(A)

        head = 0
        res = tail - head

        while tail < len(A):
            tail += 1
            while tail < len(A) and A[tail] != 0:
                tail += 1

            while A[head] != 0:
                head += 1

            head += 1
            tmp_res = tail - head
            if tmp_res > res:
                res = tmp_res

        return res
