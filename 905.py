class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        head = 0
        tail = len(A) - 1

        while head < tail:
            while head < tail and A[head] % 2 == 0:
                head += 1
            while head < tail and A[tail] % 2 == 1:
                tail -= 1

            if head < tail:
                A[head], A[tail] = A[tail], A[head]

        return A
