class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        head = 0
        tail = len(A) - 1

        res = [0] * len(A)
        res_tail = len(res) - 1

        while res_tail >= 0:
            if A[head] * A[head] > A[tail] * A[tail]:
                res[res_tail] = A[head] * A[head]
                head += 1
                res_tail -= 1
            else:
                res[res_tail] = A[tail] * A[tail]
                tail -= 1
                res_tail -= 1

        return res
