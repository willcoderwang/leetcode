class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return Solution.peak_index_in_mountain_array_core(A)

    @staticmethod
    def peak_index_in_mountain_array_core(A, start=0, stop=None):
        if stop is None:
            stop = len(A)

        # if length is short enough, use the simple method
        if stop - start < 10:
            return Solution.peak_index_in_mountain_array_simple(A, start, stop)

        one_third = int((stop - start) / 3)
        head = start + one_third
        tail = stop - one_third

        if A[start] > max(A[head], A[tail], A[stop-1]):
            return Solution.peak_index_in_mountain_array_core(A, start, head)

        if A[head] > max(A[start], A[tail], A[stop-1]):
            return Solution.peak_index_in_mountain_array_core(A, start, tail)

        if A[tail] > max(A[start], A[head], A[stop-1]):
            return Solution.peak_index_in_mountain_array_core(A, head, stop)

        if A[stop-1] > max(A[head], A[start], A[tail]):
            return Solution.peak_index_in_mountain_array_core(A, tail, stop)

    @staticmethod
    def peak_index_in_mountain_array_simple(A, start=0, stop=None):
        if stop is None:
            stop = len(A)

        for i in range(start, stop-1):
            if A[i] > A[i+1]:
                return i

        else:
            return stop - 1
