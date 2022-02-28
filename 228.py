class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        results = []
        start, end = None, None

        for n in nums:
            if end is not None and end + 1 == n:
                end = n
                continue

            if end is not None:
                if start == end:
                    results.append(str(start))
                else:
                    results.append(f"{start}->{end}")

            start, end = n, n

        if end is not None:
            if start == end:
                results.append(str(start))
            else:
                results.append(f"{start}->{end}")
        return results
